import imdb
import database
from datetime import datetime


def adaugare_serial(link, score):
    link_imdb = link
    title, episodes = imdb.get_informations(link.replace(" ", ""))
    print("Numarul de episoade al serialului "+title+" este "+episodes)
    last_episode = input("Care a fost ultimul episod vazut ? : ")
    date_entry = input("Introdu data in care ai vazut ultimul episod (Format:year-month-day-hour) sau today :")
    if date_entry.find("today") != -1:
        last_view = datetime.now()
    else:
        year, month, day, hour = map(int, date_entry.split('-'))
        last_view = datetime(year, month, day, hour)
    snooze = 0
    database.add_serie(title, episodes, int(score), link_imdb, last_episode, last_view, snooze)


def listare():
    database.print_series()


def delete_serie(title):
    database.delete_serie(title)


def snooze_serie(title):
    database.snooze_serie(title)


def unsnooze_serie(title):
    database.unsnooze_serie(title)


def modify_score(title, score):
    database.update_score(title, score)
