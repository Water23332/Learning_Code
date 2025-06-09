import sqlite3
from pathlib import Path

# Progress: initializing 2 sql databases and a corresponding table
# TODO: using the data from importer.py to populate those tables with yomichan data
def init_sql_databases():
    db_folder = "db"
    project_root = Path(__file__).parent
    dict_db_filename = "japanese_dict.db"
    freq_db_filename = "freq.db"
    dict_db_path = project_root / db_folder / dict_db_filename
    freq_db_path = project_root / db_folder / freq_db_filename
    
    # database 1: dict
    with sqlite3.connect(dict_db_path) as conn:
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
            print(f"dictionary database sucefully created or it already exists")
        except sqlite3.Error as e:
            print(f"sqlite error occurred: {e}")
            exit()

    # database 2: freq
    with sqlite3.connect(freq_db_path) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS dict (
                id INTEGER PRIMARY KEY AUTOINCREMENT, --idk if i need this (an id) at all, but fuck it, maybe for later
                term TEXT NOT NULL,
                freq INTEGER UNIQUE
            )
            ''')
            print(f"freq database sucefully created or it already exists")
        except sqlite3.Error as e:
            print(f"sqlite error occurred: {e}")
            exit()

init_sql_databases()