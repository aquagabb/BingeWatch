import sqlite3


def create_table():
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


def create_table_youtube():
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    # CREATE TABLE TVseries
    sqlite_create_table_query = """CREATE TABLE IF NOT EXISTS youtube (
                                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                                               title TEXT NOT NULL,
                                               season INTEGER NOT NULL,
                                               episode INTEGER NOT NULL,
                                               linkYoutube TEXT NOT NULL
                                               )"""
    cursor.execute(sqlite_create_table_query)
    connection.commit()
    cursor.close()


def add_serie(title, episodes, score, link_imdb, last_episode, last_view, snooze):
    try:
        connection = sqlite3.connect('imdb.db')
        cursor = connection.cursor()
        # INSERT INTO TVSERIES
        sqlite_insert_with_param = """INSERT INTO 'series'
                          ('title', 'episodes', 'score', 'linkImdb', 'lastEpisode', 'lastView' ,'snooze') 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""

        data_tuple = (title, episodes, score, link_imdb, last_episode, last_view, snooze)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)


def delete_serie(title):
    try:
        connection = sqlite3.connect('imdb.db')
        cursor = connection.cursor()
        sql_delete_query = """DELETE from series where title = ?"""
        cursor.execute(sql_delete_query, (title,))
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from a sqlite table", error)


def snooze_serie(title):
    try:
        connection = sqlite3.connect('imdb.db')
        cursor = connection.cursor()
        sql_update_query = """UPDATE series SET snooze = 1 WHERE title = ?"""
        cursor.execute(sql_update_query, (title,))
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)


def modify_episode(title, episode):
    try:
        connection = sqlite3.connect('imdb.db')
        cursor = connection.cursor()
        sql_update_query = """UPDATE series SET lastEpisode = ? WHERE title = ?"""
        cursor.execute(sql_update_query, (episode, title,))
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)


def unsnooze_serie(title):
    try:
        connection = sqlite3.connect('imdb.db')
        cursor = connection.cursor()
        sql_update_query = """UPDATE series SET snooze = 0 WHERE title = ?"""
        cursor.execute(sql_update_query, (title,))
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)


def update_score(title, score):
    try:
        connection = sqlite3.connect('imdb.db')
        cursor = connection.cursor()
        sql_update_query = """UPDATE series SET score = ? WHERE title = ?"""
        cursor.execute(sql_update_query, (score, title,))
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)


def get_all_series():
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * FROM series ORDER BY score DESC"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records


def get_series():
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT title,episodes,score,linkImdb,lastEpisode,snooze
                             FROM series 
                             WHERE snooze= 0
                             ORDER BY score DESC"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records


def get_series_snooze():
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT title,snooze
                             FROM series 
                             WHERE snooze= 1
                             ORDER BY score DESC"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records


def update_episodes(title, episodes):
    try:
        connection = sqlite3.connect('imdb.db')
        cursor = connection.cursor()
        sql_update_query = """UPDATE series SET episodes = ? WHERE title = ?"""
        cursor.execute(sql_update_query, (episodes, title,))
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)


def add_video_youtube(title, season, episodes, link_youtube):
    try:
        connection = sqlite3.connect('imdb.db')
        cursor = connection.cursor()
        sqlite_insert_with_param = """INSERT INTO 'youtube'
                          ('title', 'season', 'episode', 'linkYoutube') 
                          VALUES (?, ?, ?, ?);"""

        data_tuple = (title, season, episodes, link_youtube)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)


def print_youtube():
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * FROM youtube"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    cursor.close()
    return records
