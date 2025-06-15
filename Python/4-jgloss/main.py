from search import kanji_search
import sys

# Progress: calling upon importer.py, inserting a single term into the database
# TODO: 

def main():
    cli_input = sys.argv[1]
    print(kanji_search(cli_input))

main()