import sqlite3
from datetime import datetime

DB_NAME = "chat_history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            sender TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_message(sender, message):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (timestamp, sender, message) VALUES (?, ?, ?)",
                   (datetime.now().isoformat(), sender, message))
    conn.commit()
    conn.close()

def get_all_messages():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, sender, message FROM history ORDER BY id ASC")
    messages = cursor.fetchall()
    conn.close()
    return messages
