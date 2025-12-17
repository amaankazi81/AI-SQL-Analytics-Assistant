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
   - **Project Architecture:**
      ```
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

---

## 📂 Project Structure
   - **Project Structure is as follow:**
      ```
        AI-SQL-Analytics-Assistant/
        │
        ├── app.py               # Streamlit application
        ├── database.py          # DB connection & engine
        ├── agent.py             # LangChain SQL Agent logic
        ├── requirements.txt     # Python dependencies
        ├── .env                 # Environment variables
        └── README.md            # Project documentation


## ⚙️ Installation & Setup

  1. **Clone the repository**
      ```
        git clone https://github.com/amaankazi81/AI-SQL-Analytics-Assistant.git
        cd AI-SQL-Analytics-Assistant

  2. **Create virtual environment**
      ```
        python -m venv venv

  3. **Activate virtual environment (Windows)**
      ```
        source venv/Scripts/activate

  4. **Install dependencies**
      ```
        pip install -r requirements.txt

  5. **Run the Streamlit application**
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
