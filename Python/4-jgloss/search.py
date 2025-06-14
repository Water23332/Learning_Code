from importer import db_connect

def kanji_search(kanji_input):
    dict_conn = db_connect()[0]
    dict_cursor = db_connect()[1]

    #dict_conn, dict_cursor, = 

    dict_cursor.execute("""
        SELECT kanji, kana, definition
        FROM dict
        WHERE kanji = ?
    """, (kanji_input))

    result = dict_cursor.fetchall()

    dict_conn.close()

    return result
    
if __name__ == "__main__":
    # everything after and including this is test code, it wont be run when imported, but will be run when the file is called in terminal#
    kanji_input = "日"
    result = kanji_search(kanji_input)
    print(result)