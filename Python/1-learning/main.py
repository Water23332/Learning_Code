import sqlite3
from pathlib import Path

db_filename = "japanese_dict.db"
project_root = Path(__file__).parent
db_path = project_root / db_filename

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dict (
            kanji TEXT,
            kana TEXT,
            katakana TEXT,
            definition TEXT    
        )
    ''')
except sqlite3.Error as e:
    print(f"sqlite error occurred: {e}")
    exit()