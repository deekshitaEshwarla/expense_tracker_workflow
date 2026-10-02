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

        for ind_category in DEFAULT_CATEGORIES:
            conn.execute("INSERT OR IGNORE INTO categories (cat_name) VALUES (?)", (ind_category,))
        
        conn.commit()
    finally:
        conn.close()

def add_expense(new_category, new_amount_paise, new_spent_on):
    conn = sqlite3.connect(DB_PATH)
    try :
        cursor = conn.execute("INSERT INTO expenses(category, amount_paise, spent_on) VALUES (?,?,?)", (new_category, new_amount_paise, new_spent_on))
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()