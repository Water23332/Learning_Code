from zipfile import ZipFile, BadZipFile
from pathlib import Path

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
    with ZipFile(dictPath, 'r') as df: # short for 'dictionary file'
        for zipContents in df.namelist():
            print(f"this file has been found: {zipContents}")
            if zipContents.startswith("term_bank"):
                print("-> this is a yomichan term bank")  # TODO left here
except BadZipFile:
    print(f"the given dictionary in {dictPath} is not a real zip file")
    exit()
except Exception:
    print(f"unkown error {Exception}")
    exit()
