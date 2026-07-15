import sqlite3
import threading

# 1. This will trigger a CRITICAL rule-based finding (Hardcoded Secret)
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

# 2. This will trigger a HIGH rule-based finding (SQL Injection)
def get_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

# 3. This will trigger a MEDIUM rule-based finding (Swallowed Exception)
def do_something():
    try:
        print("doing work")
    except Exception:
        pass

# 4. This will trigger the LLM to find a Logic Bug / Race Condition
counter = 0
def increment_counter():
    global counter
    for _ in range(10000):
        counter += 1
