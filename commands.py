import request

import database
from datetime import datetime


def adaugare_serial(link, score):
    link_imdb = link
    title, episodes = request.get_informations(link.replace(" ", ""))
    if title != "" and episodes != "":
        print("Numarul de episoade al serialului " + title + " este " + episodes)
        last_episode = input("Care a fost ultimul episod vazut ? : ")
        date_entry = input("Introdu data in care ai vazut ultimul episod (Format:year-month-day-hour) sau today : ")
        if date_entry.find("today") != -1:
            last_view = datetime.now()
        else:
            year, month, day, hour = map(int, date_entry.split('-'))
            last_view = datetime(year, month, day, hour)
        snooze = 0
        database.add_serie(title, episodes, int(score), link_imdb, last_episode, last_view, snooze)
        seasons, new_link = request.get_numberOfSeasons(link)
        number_seasons = int(seasons)
        suma_episoadelor = int(episodes)
        ok = 0
        last_episode_viewed = int(last_episode)
        while number_seasons > 0 and ok == 0:
            link_episodes = 'https://www.imdb.com' + new_link + str(number_seasons)
            number_episodes = request.get_numberOfEpisodes_season(link_episodes)
            if suma_episoadelor >= last_episode_viewed >= suma_episoadelor - int(
                    number_episodes):
                episod_din_sezon = int(last_episode_viewed) - (suma_episoadelor - int(number_episodes))
                query = title + ' season ' + str(number_seasons) + ' episode ' + str(episod_din_sezon)
                link_youtube = request.videos_youtube(query)
                database.add_video_youtube(title, number_seasons, episod_din_sezon, link_youtube)
                ok = 1
            else:
                suma_episoadelor = suma_episoadelor - int(number_episodes)
            number_seasons = number_seasons - 1
    else:
        print("Nu s-a putut face request de la IMDB")
    print(database.print_youtube())


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


def get_series():
    list_series = database.get_series()
    for serie in list_series:
        print(serie)
    for serie in list_series:
        title = serie[0]
        current_episodes = int(serie[1])
        score = serie[2]
        link = str(serie[3])
        last_episode = serie[4]
        new_episodes = int(request.get_episodes(link))
        if current_episodes < new_episodes:
            print("Titlul serialului :" + title)
            print("Scorul : " + str(score))
            print("Numarul vechi de episoade " + str(current_episodes))
            print("Numarul nou de episoade " + str(new_episodes))
            print("Ultimul episod pe care l-ai vazut a fost : " + str(last_episode))
            print("Au mai aparut " + str(new_episodes - current_episodes) + " episoade noi")
            print("=======================================================================")
            # database.update_episodes(title,new_episodes)
        elif new_episodes == 0:
            print("Nu s-a putut face request de la IMDB")

