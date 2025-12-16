import streamlit as st
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent


# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


# Streamlit UI
st.set_page_config(page_title="AtliQ Tees AI SQL Agent", layout="wide")
st.title("👕 AtliQ Tees – AI Store Manager (SQL Agent)")

st.markdown(
    """
Ask questions in **plain English**.  
The AI agent will automatically:
- Understand the database schema
- Generate correct SQL
- Execute it safely
- Return the answer
"""
)


# Database Initialization
@st.cache_resource
def init_db():
    engine = create_engine(
        f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    )
    return SQLDatabase(engine)

db = init_db()


# Gemini LLM 
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0,
    google_api_key=GOOGLE_API_KEY
)


# SQL AGENT 
agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)


# User Input
question = st.text_input(
    "Ask a question 👇",
    placeholder="How many Adidas t shirts are there in stock?"
)


# Run Agent
if st.button("Ask AI"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = agent.run(question)

                st.subheader("✅ Answer")
                st.success(response)

            except Exception as e:
                st.error("Error while processing your query.")
                st.exception(e)
