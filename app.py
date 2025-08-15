from flask import Flask, jsonify, request, render_template_string
import os
import mysql.connector
import time

app = Flask(__name__)

db_config = {
    "host": os.getenv("MYSQL_HOST", "mysql"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "password"),
    "database": os.getenv("MYSQL_DATABASE", "test_db")
}

# Retry connection function
def connect_with_retry(retries=10, delay=3):
    for i in range(retries):
        try:
            conn = mysql.connector.connect(**db_config)
            return conn
        except mysql.connector.Error as err:
            print(f"MySQL not ready yet, retrying ({i+1}/{retries})...")
            time.sleep(delay)
    raise Exception("Could not connect to MySQL after several attempts.")

# Create table if not exists
def init_db():
    conn = connect_with_retry()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Notes App</title>
</head>
<body>
    <h1>Notes</h1>
    <form method="POST">
        <textarea name="content" placeholder="Write your note here..." required></textarea><br>
        <button type="submit">Save Note</button>
    </form>
    <hr>
    <h2>Saved Notes:</h2>
    <ul>
        {% for note in notes %}
            <li>{{ note[1] }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    conn = connect_with_retry()
    cursor = conn.cursor()

    if request.method == "POST":
        content = request.form["content"]
        cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
        conn.commit()

    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = cursor.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
