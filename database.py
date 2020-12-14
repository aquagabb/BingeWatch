import sqlite3


def create_table():
    """
           Se conecteaza la baza de date si se creeaza tabela 'series' in care se vor stoca informatiile despre seriale
    """
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
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
    """
       Se conecteaza la baza de date si se creeaza tabela 'youtube' in care se va stoca titli,ultimul episod vazut
       dintr-un anume sezon si link-ul de pe youtube cu query-ul facut
    """
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
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
    """
        Se conecteaza la baza de date si se face un insert cu informatiile despre un serial in tabela 'series'
    """
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
    """
          Primeste ca parametru titlu serialui care doreste utilizatorul sa fie sters si va fi eliminat din tabela
          series
    """
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
    """
           Primeste ca parametru titlu serialui si se va face un update pe snooze=1 pe serialul respectiv.
    """
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
    """
       Primeste ca parametru titlu serialui si episodul pe care il doreste utilizatorul sa fie modificat.Se va face un
       update pentru ultimul episod vazut.
    """
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
    """
               Primeste ca parametru titlu serialui si se va face un update pe snooze=0 pe serialul respectiv.
    """
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
    """
       Primeste ca parametru titlu serialui si scorul pe care il doreste utilizatorul sa il modifice.Se va face un
       update pentru scorul ales al serialului respectiv.
    """
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
    """
           Va returna toate liniile din tabela series ordonate descrescator dupa scor
    """
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * FROM series ORDER BY score DESC"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records


def get_series():
    """
        Va returna datele din tabela series ordonate descrescator dupa scor unde serialele nu sunt pe snooze.
    """
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
    """
            Va returna datele din tabela series ordonate descrescator dupa scor unde serialele sunt pe snooze.
    """
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
    """
         Primeste ca parametru titlu serialui si numarul de episoade pe care il va modifica in baza de date.Comanda se
         foloseste atunci cand dupa un request numarul de episoade nu este acelasi cu cel din baza de date.
    """
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
    """
        Primeste ca parametri informatiile specifice unui query catre youtube + link-ul catre " Title season x episode y
    """
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
    """
         Functia returneaza datele din tabela youtube.
    """
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * FROM youtube"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    cursor.close()
    return records

