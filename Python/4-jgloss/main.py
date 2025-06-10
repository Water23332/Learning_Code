import sqlite3
from pathlib import Path
from importer import *

# Progress: calling upon importer.py, inserting a single term into the database
# TODO: inserting all terms and making the import dictionary part something on its own

def main():
    term_data = extract_termdata_from_zip()
    for i in term_data[356]:
        for a in i:
            print(a)
    
if __name__ == "__main__":
    main()
