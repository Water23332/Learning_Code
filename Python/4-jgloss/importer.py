from zipfile import ZipFile, BadZipFile
from pathlib import Path
import io
import json
import sqlite3

# Progress: modulating this into a function
# TODO: adding this to main


def find_zip_dict():
    dictionaryFolder = Path('dictionaries')
    try:
        dictFile = next(dictionaryFolder.glob("*.zip"))
        return dictFile
    except StopIteration:
        print("Error: No dictionary .zip file found in the 'dictionaries' folder.")
        exit()

def extract_termdata_from_zip(): # returns 'termData'
    dictPath = find_zip_dict()
    try:
        with ZipFile(dictPath, 'r') as zf:
            archiveContents = zf.namelist()
            for Content in archiveContents:
                if Content.startswith("term_bank"):
                    with zf.open(Content) as termbank_file_obj:
                        print(f"termbank file successfully opened!!")
                        try:
                            text_file_obj = io.TextIOWrapper(termbank_file_obj, encoding='utf-8')
                            jsonData = json.load(text_file_obj)
                            if jsonData is None:
                                return [] #needed for error handling
                            return jsonData #retuns as tuple, where index 5 (so the 6th item), the definition, also itself is a tuple
                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON from {termbank_file_obj}: {e}")
                        except Exception as e:
                            print(f"An error occurred processing {termbank_file_obj}: {e}")
    except BadZipFile:
        print(f"the given dictionary in {dictPath} is not a real zip file")
        exit()
    except Exception:
        print(f"unkown error {Exception}")
        exit()
    return []  # Return empty list if no termbank file found
    db_folder = "db"
    project_root = Path(__file__).parent
    freq_db_filename = "freq.db"
    freq_db_path = project_root / db_folder / freq_db_filename
    with sqlite3.connect(freq_db_path) as conn:
        cursor = conn.cursor()
        return cursor

def create_sql_databases():
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
                definition TEXT NOT NULL
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
            CREATE TABLE IF NOT EXISTS freq (
                id INTEGER PRIMARY KEY AUTOINCREMENT, --idk if i need this (an id) at all, but fuck it, maybe for later
                term TEXT NOT NULL,
                freq INTEGER UNIQUE
            )
            ''')
            print(f"freq database sucefully created or it already exists")
        except sqlite3.Error as e:
            print(f"sqlite error occurred: {e}")
            exit()

def insert_bulk_term(db_cursor, kanji, kana, definition):
    # Convert definition list to string if it's a list
    if isinstance(definition, list):
        definition = '; '.join(definition)
        
    insert_term_sql = """
        INSERT INTO dict (kanji, kana, definition)
        VALUES (?, ?, ?)
    """
    values = [(kanji, kana, definition)]
    db_cursor.executemany(insert_term_sql, values)

def insert_bulk_freq(db_cursor, term, freq):
    freq_freq_sql = """
        INSERT INTO freq (term, freq)
        VALUES (?, ?,);
    """
    db_cursor.executemany(freq_freq_sql, term, freq)

    return 42

if __name__ == "__main__":
    #everything after and including this is test code, it wont be run when imported, but will be run when the file is called in terminal#
    print("")