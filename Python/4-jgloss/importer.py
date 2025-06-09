from zipfile import ZipFile, BadZipFile
from pathlib import Path
import io
import json

# file finder
dictionaryFolder = Path('dictionaries')
try:
    dictPath = next(dictionaryFolder.glob("*.zip"))
    print(f"zip file found: {dictPath}")
except StopIteration:
    print("Error: No dictionary .zip file found in the 'dictionaries' folder.")
    exit()

# extractor
termBanksData = []

try:
    with ZipFile(dictPath, 'r') as zf: # short for 'dictionary file'
        archiveContents = zf.namelist()
        for Content in archiveContents:
            print(f"this file has been found: {Content}")
            if Content == "index.json":
                with zf.open(Content) as index_file_obj:
                    print(f"-> index file opened!!")
                    print(index_file_obj.read())
            elif Content.startswith("term_bank"):
                with zf.open(Content) as termbank_file_obj:
                    print(f"-> termbank file opened!!")
except BadZipFile:
    print(f"the given dictionary in {dictPath} is not a real zip file")
    exit()
except Exception:
    print(f"unkown error {Exception}")
    exit()
