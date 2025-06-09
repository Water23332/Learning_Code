import sqlite3
from pathlib import Path
from importer import extract_termdata_from_zip, create_sql_databases, insert_bulk_term #, insert_bulk_freq

# Progress: calling upon importer.py, inserting a single term into the database
# TODO: inserting all terms and making the import dictionary part something on its own

def main():
    # Initialize databases
    term_data = extract_termdata_from_zip()

    db_folder = "db"
    project_root = Path(__file__).parent
    dict_db_filename = "japanese_dict.db"
    #freq_db_filename = "freq.db"
    dict_db_path = project_root / db_folder / dict_db_filename
    #freq_db_path = project_root / db_folder / freq_db_filename
    create_sql_databases()

    conn = sqlite3.Connection(dict_db_path)
    cursor = conn.cursor()
    try:
        for term_single in term_data:
            insert_bulk_term(cursor, term_single[0], term_single[1], term_single[5])
        conn.commit()
        print("Successfully inserted all terms!")
    except Exception as e:
        print(f"failure: {e}")
        exit()

#if __name__ == "__main__":
main()