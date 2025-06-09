import sqlite3
from pathlib import Path

db_filename = "japanese_dict.db"
project_root = Path(__file__).parent
db_path = project_root / db_filename

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS dict (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kanji TEXT NOT NULL,
            kana TEXT NOT NULL,
            def TEXT NOT NULL
        )
        ''')
    except sqlite3.Error as e:
        print(f"sqlite error occurred: {e}")
        exit()