# 💻 SQL Injection Demo (Flask-based Educational App)

A Python-based web application built using Flask to demonstrate both **vulnerable** and **secure** SQL query handling. This project is intended for educational purposes to help learners understand how SQL Injection attacks work — and how to prevent them using parameterized queries.

---

## 🚀 Features

- Web interface with login form
- 🔴 Vulnerable query using string formatting
- ✅ Secure query using parameterized statements
- SQLite database for storing user credentials
- Demonstrates how SQL Injection can bypass login
- Educational and beginner-friendly

---

## 🧱 Tech Stack

- Python 3.x
- Flask
- SQLite3
- HTML (Flask templates)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/SnehaSadhukhan/Sql_Injection_Demo.git
cd Sql_Injection_Demo
```
## Install dependencies:

```bash
pip install -r requirements.txt
```
## ▶️ Usage
Run the Flask app:
1. ```bash
   python app.py
   ```
2. Open your browser and go to:
    http://127.0.0.1:5000/
3. Try logging in with:
    Username: ' OR '1'='1
    Password: anything
4. Comment/uncomment lines in app.py to toggle between:
   Insecure (string formatting)
   Secure (parameterized ? syntax)

