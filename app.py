from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# DB Initialization
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL)''')
    # Insert sample user (only once)
    c.execute("SELECT * FROM users WHERE username='admin'")
    if not c.fetchone():
        c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # 🚨 VULNERABLE QUERY (for demonstration only)
        # query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        # print("Executing:", query)  # You’ll see SQL injection here
        # c.execute(query)

        # ✅ SAFE VERSION (comment out the vulnerable one above and uncomment this to fix)
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

        result = c.fetchone()
        conn.close()

        if result:
            return "✅ Login Successful"
        else:
            return "❌ Invalid Credentials"

    return render_template('login.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
