from zipfile import ZipFile, BadZipFile
from pathlib import Path
import io
import json
import sqlite3

# Progress: importing terms
# TODO: importing freq, importing different dictionaries (maybe inside another table that tracks imported dictionaries? maybe also appending the dictionary to every term in the dict_db)

# Database vars

def db_connect():
    db_folder = "db"
    dict_db_filename = "japanese_dict.db"
    freq_db_filename = "freq.db"
    project_root = Path(__file__).parent
    dict_db_path = project_root / db_folder / dict_db_filename
    freq_db_path = project_root / db_folder / freq_db_filename

    # Sqlite connection; these lines also automatically create the .db files
    dict_conn = sqlite3.connect(dict_db_path)
    dict_cursor = dict_conn.cursor()
    freq_conn = sqlite3.connect(freq_db_path)
    freq_cursor = freq_conn.cursor()

    # Return connections and cursors
    return dict_conn, dict_cursor, freq_conn, freq_cursor

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
                        print(f"termbank file successfully opened ✅")
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

def create_sql_databases(dict_cursor, dict_conn, freq_cursor, freq_conn):
    # Check
    try:
        dict_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dict'")
        freq_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='freq'")
        if dict_cursor.fetchone() and freq_cursor.fetchone():
            print("Table 'dict' and 'freq' do exist in the dictionary database. Skipping database creation ⏩")
            return # ends it prematurely 
    except sqlite3.Error as e:
        print(f"sqlite error occurred whilst checking if database exists: {e}")
        exit()

    # database 1: dict
    try:
        dict_cursor.execute('''
        CREATE TABLE IF NOT EXISTS dict (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kanji TEXT NOT NULL,
            kana TEXT NOT NULL,
            definition TEXT NOT NULL
        )
        ''')
        dict_conn.commit()
        #dict_conn.close()
        print(f"dictionary database sucefully created ✅")
    except sqlite3.Error as e:
        print(f"sqlite error occurred whilst creating term_database: {e}")
        exit()

    # database 2: freq
    try:
        freq_cursor.execute('''
        CREATE TABLE IF NOT EXISTS freq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            term TEXT NOT NULL,
            freq INTEGER UNIQUE
        )
        ''')
        freq_conn.commit()
        #freq_conn.close()
        print(f"freq database sucefully created ✅")
    except sqlite3.Error as e:
        print(f"sqlite error occurred whilst creating freq_database: {e}")
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
        VALUES (?, ?)
    """
    db_cursor.executemany(freq_freq_sql, term, freq)

def import_terms(dict_cursor, dict_conn):
    term_data = extract_termdata_from_zip()

    # Check if the first and last terms are already in the database
    try:
        first_term = term_data[0]
        last_term = term_data[-1]

        dict_cursor.execute("SELECT COUNT(*) FROM dict WHERE kanji = ? AND kana = ?", (first_term[0], first_term[1]))
        first_term_exists = dict_cursor.fetchone()[0] > 0

        dict_cursor.execute("SELECT COUNT(*) FROM dict WHERE kanji = ? AND kana = ?", (last_term[0], last_term[1]))
        last_term_exists = dict_cursor.fetchone()[0] > 0

        if first_term_exists and last_term_exists:
            print("Terms already imported. Skipping import ⏩")
            return
    except Exception as e:
        print(f"im too lazy to specify this error: {e}")
        exit(1)

    # Proceed with importing terms if not already imported
    for term in term_data:
        insert_bulk_term(dict_cursor, term[0], term[1], term[5])  # [0] kanji, [1] kana, [5] definition
    
    dict_conn.commit()
    dict_conn.close()

    print("import success ✅")


if __name__ == "__main__":
    # everything after and including this is test code, it wont be run when imported, but will be run when the file is called in terminal#
    ## Vars
    dict_conn, dict_cursor, freq_conn, freq_cursor = db_connect()

    ## Creaton
    create_sql_databases(dict_cursor, dict_conn, freq_cursor, freq_conn)

    ## Import term
    import_terms(dict_cursor, dict_conn)