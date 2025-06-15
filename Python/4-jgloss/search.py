from importer import db_connect

def kanji_search(kanji_input):
    dict_conn = db_connect()[0]
    dict_cursor = db_connect()[1]

    dict_cursor.execute("""
        SELECT definition
        FROM dict
        WHERE kanji = ?
    """, (kanji_input,)) # Note the comma to make it a tuple

    result = dict_cursor.fetchall()
    dict_conn.close()
    return result
    
if __name__ == "__main__":
    print(kanji_search("本日"))
