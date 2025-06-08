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
    with ZipFile(dictPath, 'r') as df: # short for 'dictionary file'
        archiveContents = df.namelist()
        for Content in archiveContents:
            print(f"this file has been found: {Content}")
            if Content == "index.json":
                print("-> this is a yomichan term index")
                with df.open(Content, 'r') as file:
                    print(f"Opened {Content} from ZIP.")
            elif Content.startswith("term_bank"):
                print("-> this is a yomichan term bank")
                with df.open(Content, 'r') as file_in_zip:
                    #TODO #left here
                # Process term_bank_file_obj
                print(f"Opened {Content} from ZIP.")
                # Content will be read in the next step
except BadZipFile:
    print(f"the given dictionary in {dictPath} is not a real zip file")
    exit()
except Exception:
    print(f"unkown error {Exception}")
    exit()
