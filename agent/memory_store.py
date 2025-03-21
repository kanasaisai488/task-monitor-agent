
# Module: memory_store.py
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "../storage/memory.sqlite")

def init_memory_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS task_memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            project_tag TEXT,
            task_description TEXT,
            file_path TEXT,
            diff TEXT,
            prompt_block TEXT,
            status TEXT,
            special_instructions TEXT
        )
    """)
    conn.commit()
    conn.close()

def store_task_record(project_tag, task_description, file_path, diff, prompt_block, status="pending", special_instructions=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO task_memory (timestamp, project_tag, task_description, file_path, diff, prompt_block, status, special_instructions)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        project_tag,
        task_description,
        file_path,
        diff,
        prompt_block,
        status,
        special_instructions
    ))
    conn.commit()
    conn.close()

def fetch_all_records(project_tag=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if project_tag:
        c.execute("SELECT * FROM task_memory WHERE project_tag = ?", (project_tag,))
    else:
        c.execute("SELECT * FROM task_memory")
    rows = c.fetchall()
    conn.close()
    return rows

def update_task_status(task_id, new_status):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE task_memory SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    conn.close()

def log_dispatched_context(component, context_snippet, project_tag="TaskMonitorAgent"):
    db_path = os.path.join(os.getcwd(), "task_memory.db")  # adjust path if needed

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dispatched_context_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                project TEXT,
                component TEXT,
                context_snippet TEXT
            )
        ''')

        cursor.execute('''
            INSERT INTO dispatched_context_log (timestamp, project, component, context_snippet)
            VALUES (?, ?, ?, ?)
        ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), project_tag, component, context_snippet[:5000]))  # limit for safety

        conn.commit()
        conn.close()
        print(f"📥 Logged dispatched context for: {component}")

    except Exception as e:
        print(f"⚠️ Error logging dispatched context: {e}")
