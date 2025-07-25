import sqlite3
import os
from datetime import datetime
import csv

# Diretório para armazenar o banco
DB_DIR = "data"
DB_NAME = "chat_history.db"
DB_PATH = os.path.join(DB_DIR, DB_NAME)

# Garante que o diretório exista
os.makedirs(DB_DIR, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
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
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (timestamp, sender, message) VALUES (?, ?, ?)",
                   (datetime.now().isoformat(), sender, message))
    conn.commit()
    conn.close()

def get_all_messages():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, sender, message FROM history ORDER BY id ASC")
    messages = cursor.fetchall()
    conn.close()
    return messages

def clear_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history")
    conn.commit()
    conn.close()

# Opcional: manter para exportar com caminho fixo
def export_to_csv(filename="chat_history.csv"):
    messages = get_all_messages()
    with open(filename, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Sender", "Message"])
        writer.writerows(messages)
