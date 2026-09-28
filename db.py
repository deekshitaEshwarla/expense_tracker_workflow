import sqlite3 
from pathlib import Path


HERE = Path(__file__).parent
DB_PATH = HERE / "expenses.db"
SCHEMA_PATH = HERE / "schema.sql"
DEFAULT_CATEGORIES = ["groceries", "milk", "stationery"]


def init_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        schema_sql = SCHEMA_PATH.read_text()
        conn.executescript(schema_sql)
        for category in DEFAULT_CATEGORIES:
            conn.execute("INSERT OR IGNORE INTO categories (cat_name) VALUES (?)", (category,))
        
        conn.commit()
    finally:
        conn.close()