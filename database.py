import sqlite3

def createTable():
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    # CREATE TABLE TVseries
    sqlite_create_table_query = """CREATE TABLE IF NOT EXISTS series (
                                           title TEXT PRIMARY KEY,
                                           episodes INTEGER NOT NULL,
                                           score INTEGER NOT NULL,
                                           linkImdb TEXT NOT NULL,
                                           lastEpisode INTEGER,
                                           lastView date,
                                           snooze INTEGER
                                           )"""
    cursor.execute(sqlite_create_table_query)
    connection.commit()
    cursor.close()

def addSerie(title, episodes, score, linkImdb, lastEpisode, lastviewDate, snooze):
    try:
        connection = sqlite3.connect('imdb.db')
        cursor = connection.cursor()
        # INSERT INTO TVSERIES
        sqlite_insert_with_param = """INSERT INTO 'series'
                          ('title', 'episodes', 'score', 'linkImdb', 'lastEpisode', 'lastView' ,'snooze') 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""

        data_tuple = (title, episodes, score, linkImdb, lastEpisode, lastviewDate, snooze)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)

def printSeries():
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * from series"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print(records)
    cursor.close()

