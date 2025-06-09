from zipfile import ZipFile, BadZipFile
from pathlib import Path
import io
import json

# Progress: wrapping the json data inside the dictionary zip file into an object
# TODO: using that data for the sql database -> modulating this into a function

# file finder
def find_zip_dict():
    dictionaryFolder = Path('dictionaries')
    try:
        dictFile = next(dictionaryFolder.glob("*.zip"))
        return dictFile
    except StopIteration:
        print("Error: No dictionary .zip file found in the 'dictionaries' folder.")
        exit()

# extractor
termBanksData = []

#def import_zip_to_sql(): 
dictPath = find_zip_dict()
try:
    with ZipFile(dictPath, 'r') as zf: # short for 'dictionary file'
        archiveContents = zf.namelist()
        for Content in archiveContents:
            #print(f"this file has been found: {Content}")
            if Content.startswith("term_bank"):
                with zf.open(Content) as termbank_file_obj:
                    print(f"-> termbank file opened!!")
                    try:
                        text_file_obj = io.TextIOWrapper(termbank_file_obj, encoding='utf-8')
                        data = json.load(text_file_obj)
                        #print(data)
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
