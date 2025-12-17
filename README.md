# 🧠 AI-SQL-Analytics-Assistant
An AI-driven SQL analytics assistant that allows users to query a MySQL database using plain English. Built using LangChain SQL Agent, LLM, and Streamlit, this system automatically converts natural language questions into SQL queries, executes them safely, and returns human-readable answers.

---

## 🚀 Features

🔤 Natural Language → SQL query generation

🧠 Agent-based reasoning using LangChain SQL Agent

🗄️ Automatic schema understanding (no hardcoding)

📊 Inventory, sales, and discount analytics

🔐 Safe, read-only SQL execution

⚡ Real-time responses via Streamlit UI

🔄 LLM-agnostic design (Gemini / OpenAI compatible)

---

## 🏗️ Architecture Overview

User (English Query)
    ↓
Streamlit UI
    ↓
LangChain SQL Agent
    ↓
LLM Reasoning
    ↓
MySQL Database
    ↓
Query Result
    ↓
Natural Language Answer

🗄️ **Database Schema (Example)**
 
            products(product_id, brand, color, size, category)
            inventory(product_id, stock_qty)
            sales(product_id, price, discount_percentage)

---

## 🧩 Tech Stack

| Category | Technologies          |
| -------- | --------------------- |
| Language | Python                |
| Frontend | Streamlit             |
| Backend  | LangChain (SQL Agent) |
| Database | MySQL                 |
| ORM      | SQLAlchemy            |
| LLM      | OpenAI / Gemini       |
| Others   | dotenv                |


## ⚙️ Installation & Setup

  1. **Clone the Repository**
     ```
        git clone https://github.com/your-username/ai-nl-to-sql.git
        cd ai-nl-to-sql

  2 **Create Virtual Environment**
        ```
          python -m venv venv
          venv\Scripts\activate   

  3.**Install Dependencies**
        ```
          pip install -r requirements.txt

  4️ **Environment Variables**
        Create a .env file in the root directory:
        
        ```
            MYSQL_USER=root
            MYSQL_PASSWORD=your_password
            MYSQL_HOST=localhost
            MYSQL_PORT=3306
            MYSQL_DATABASE=atliq_tees

            OPENAI/GEMINI_API_KEY=your_openai/gemini_api_key

  6. **Run the Application**
        ```
          streamlit run app.py
      


## 🔐 Safety & Reliability

- ❌ No DELETE / DROP / UPDATE queries

- ✅ Read-only SELECT queries

- 🧠 Schema-aware SQL generation

- 🎯 Deterministic outputs using controlled temperature



## 🧠 Design Decisions
  
  - SQL Agent instead of SQL chains for higher accuracy and robustness
  
  - Automatic schema discovery to avoid hallucinations
  
  - Modular LLM integration for easy provider switching
  
  - Streamlit UI for rapid prototyping and interactivity


## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
