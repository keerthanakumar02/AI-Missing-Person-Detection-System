import sqlite3

conn = sqlite3.connect("missing.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    photo TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")