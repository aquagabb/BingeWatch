import sqlite3


def create_table():
    """
        Se conecteaza la baza de date si se creeaza tabela 'series' in care se vor stoca informatiile despre seriale
        :return : none
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
       :return : none
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
        :param title : titlu serialului
        :param episodes : numarul de episoade al serialului
        :param score : scorul ales de utilizator
        :param link_imdb : link-ul primit initial de la utilizator
        :param last_episode : ultimul episod ales de utilizator
        :param last_view : data la care a fost vizionat ultimul episod
        :param snooze : primeste mereu 0 by default
        :return : none
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
          Functia elimina din tabela 'series' titlul unui serial.
          :param title : titlu serialui dat ca input de utilizator
          :return : none
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
           Functia face update in tabela 'series' pe snooze=1 pentru un serial
           :param title : titlu serialui dat ca input de utilizator
           :return : none
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
       Functia face un update pentru ultimul episod vazut.
       :param title : titlul serialului
       :param episode : ultimul episod pe care doreste utilizatorul sa il modifice
       :return : none
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
        Functia face update in tabela 'series' pe snooze=0 pentru un serial
        :param title : titlu serialui dat ca input de utilizator
        :return : none
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
       Functia face un update pentru scorul ales de uitilizator pentru un serial anume.
       :param title : titlul serialului
       :param score : scorul dat ca input de utilizator pe care doreste sa il modifice
       :return : none
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
        :return : none
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
        :return : none
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
            :return : none
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
         Va modifica in baza de date numarul vechi de episoade .Comanda se foloseste atunci cand dupa un request numarul
         de episoade nu esteacelasi cu cel din baza de date.
         :param title : titlul serialului
         :param episodes : numarul de episoade nou.
         :return : none
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
        :param title : titlul serialului
        :param season : sezonul serialului
        :param episodes : episodul ales de utilizator
        :param link_youtube : link-ul dupa ce s- facut request la youtube
        :return : none
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
         :return : none
    """
    connection = sqlite3.connect('imdb.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * FROM youtube"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    cursor.close()
    return records
