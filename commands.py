import request
import database
from datetime import datetime


def adaugare_serial(link):
    """
         Se va face request la IMDB pentru a se lua titlul
         si numarul de episoade al serialului specific.Apoi utilizatorul va trebui sa completeze cateva informatii
         despre acel serial,ex:ultimul episod vazut,scorul,cand a fost vazut. Input-ul primit de utilizator va trece
         printr-o serie de verificari. In final,dupa ce se aduna toate informatiile,functia va adauga in baza de date
         in tabela 'series' dar si link-ul ultimului episod vazut in tabela 'youtube'
         :param link : Functia primeste ca parametru link-ul dat de utilizator.
         :return : none
    """
    link_imdb = link
    title, episodes = request.get_informations(link.replace(" ", ""))
    if title != "" and episodes != "":
        print("Numarul de episoade al serialului " + title + " este " + episodes)
        verificare_1 = 0
        while verificare_1 == 0:
            last_episode = input("Care a fost ultimul episod vazut ? : ")
            if 0 < int(last_episode) <= int(episodes):
                verificare_1 = 1
                date_entry = input("Introdu data in care ai vazut ultimul episod (Format:year-month-day-hour) sau "
                                   "today : ")
                if date_entry.find("today") != -1:
                    last_view = datetime.now()
                else:
                    year, month, day, hour = map(int, date_entry.split('-'))
                    last_view = datetime(year, month, day, hour)
                verificare_3 = 0
                while verificare_3 == 0:
                    score = input("Alege un scor de la 1 la 10: ")
                    if 0 < int(score) <= 10:
                        verificare_3 = 1
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
                        print("Scorul nu exista,mai incearca !")
            else:
                print("Episodul nu exista,mai incearca !")

    else:
        print("Nu s-a putut face request de la IMDB")
    print_link_youtube()


def delete_serie():
    """
           Functia va cere utilizatorului un input cu titlui serialului care doreste sa fie sters.Acesta va trece
           printr-o verificare si daca serialul exista,il va sterge din tabela 'series'.
           :return : none
    """
    list_series = database.get_all_series()
    titles = ""
    for serie in list_series:
        titles = titles + serie[0] + " ; "
    print("")
    print(titles)
    print("")
    verificare_1 = 0
    while verificare_1 == 0:
        title = input("Ce serial vrei sa stergi ? : ")
        for serie in list_series:
            title_database = serie[0]
            if title_database == title:
                verificare_1 = 1
                database.delete_serie(title)
                print("====================================")
                print("Comanda a fost efectuata cu succes !")
                print("====================================")
        if verificare_1 == 0:
            print("Serialul nu exista ,mai incearca ! ")


def snooze_serie():
    """
        Functia va cere utilizatorului un input cu titlui serialului care va trece printr-o verificare si daca serialul
        exista il va pune pe snooze daca nu este deja.
        :return : none
    """
    list_series = database.get_series()
    titles = ""
    for serie in list_series:
        titles = titles + serie[0] + "=" + str(serie[5]) + " ; "
    print("Serialele care nu sunt pe snooze")
    print(titles)
    verificare_1 = 0
    while verificare_1 == 0:
        title = input("Ce serial vrei sa pui pe snooze ? : ")
        for serie in list_series:
            title_database = serie[0]
            if title_database == title:
                verificare_1 = 1
                database.snooze_serie(title)
                print("====================================")
                print("Comanda a fost efectuata cu succes !")
                print("====================================")
        if verificare_1 == 0:
            print("Nu poti face snooze pe acest serial,mai incearca ! ")


def unsnooze_serie():
    """
        Functia va cere utilizatorului un input cu titlui serialului care va trece printr-o verificare si daca serialul
        exista il va pune pe unsnooze daca nu este deja.
        :return : none
    """
    list_series = database.get_series_snooze()
    titles = ""
    for serie in list_series:
        titles = titles + serie[0] + "=" + str(serie[1]) + " ; "
    print("Serialele care sunt deja pe snooze")
    print(titles)
    verificare_1 = 0
    while verificare_1 == 0:
        title = input("Ce serial vrei sa pui pe unsnooze ? : ")
        for serie in list_series:
            title_database = serie[0]
            if title_database == title:
                verificare_1 = 1
                database.unsnooze_serie(title)
                print("====================================")
                print("Comanda a fost efectuata cu succes !")
                print("====================================")
        if verificare_1 == 0:
            print("Nu poti face snooze pe acest serial,mai incearca ! ")


def modify_score():
    """
        Functia va cere utilizatorului un input cu titlui serialului care va trece printr-o verificare si daca serialul
        exista ii va cere un scor valid si apoi va modifica in baza de date scorul serialului ales.
        :return : none
    """
    list_series = database.get_all_series()
    titles = ""
    for serie in list_series:
        titles = titles + serie[0] + "=" + str(serie[2]) + " ; "
    print("Serialele au scorul :")
    print(titles)
    print("")
    verificare_1 = 0
    while verificare_1 == 0:
        title = input("Ce serial vrei sa modifici ? : ")
        for serie in list_series:
            title_database = serie[0]
            if title_database == title:
                verificare_1 = 1
                verificare_2 = 0
                while verificare_2 == 0:
                    score_input = input("Alege un scor de la 1 la 10: ")
                    if 0 < int(score_input) <= 10:
                        database.update_score(title, score_input)
                        verificare_2 = 1
                        print("====================================")
                        print("Comanda a fost efectuata cu succes !")
                        print("====================================")
                    else:
                        print("Scorul nu exista,mai incearca !")
        if verificare_1 == 0:
            print("Acest serial nu se afla in baza de date,mai incearca !")


def listare():
    """
        Functia va parcurge serialele din baza de date si in momentul in care numarul de episoade din baza de date
        este mai mic decat numarul de episoade primit ca request de la IMDB il va anunta pe utilizator ca au mai aparut
        X episoade in serialul Y.
        :return : none
    """
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


def modify_last_episode():
    """
       Functia va cere utilizatorului un input cu titlui serialului care va trece printr-o verificare si daca serialul
       exista ii va cere un episod valid pentru a-l modifica in baza de date. Apoi se va face un request la youtube
       cu episodul pe care a dorit sa-l modifice si il va insera link-ul query-ului in baza de date.
       :return : none
    """
    list_series = database.get_series()
    verificare_1 = 1
    while verificare_1 == 1:
        title = input("Ce serial vrei sa modifici ? : ")
        for serie in list_series:
            title_database = serie[0]
            if title_database == title:
                verificare_1 = 0
                current_episodes = int(serie[1])
                last_episode = serie[4]
                print("Numarul total de episoade : " + str(current_episodes))
                print("Ultimul episod vazut : " + str(last_episode))
                verificare_2 = 1
                while verificare_2 == 1:
                    new_last_episode = input("Episod : ")
                    if int(new_last_episode) <= current_episodes:
                        database.modify_episode(title, new_last_episode)
                        print("====================================")
                        print("Comanda a fost efectuata cu succes !")
                        print("====================================")
                        verificare_2 = 0
                        seasons, new_link = request.get_numberOfSeasons(serie[3])
                        number_seasons = int(seasons)
                        suma_episoadelor = int(current_episodes)
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
                        print("Acest episod nu exista,mai incearca !")
        if verificare_1 == 1:
            print("Acest serial nu se afla in baza de date !")


def search_youtube():
    """
        Functia cere titlul unui serial iar daca acesta exista in baza de date,utilizatorul poate sa caute pe youtube
        un anumit episod dintr-un sezon,aceasta cautare va fi inregistrata in tabela 'youtube'.
        :return : none
    """
    list_series = database.get_series()
    titles = ""
    for serie in list_series:
        titles = titles + serie[0] + ";"
    print(titles)
    verificare_1 = 0
    while verificare_1 == 0:
        title = input("Ce serial vrei sa cauti ? : ")
        for serie in list_series:
            title_database = serie[0]
            link = str(serie[3])
            if title_database == title:
                verificare_1 = 1
                list_series = database.get_series()
                seasons, new_link = request.get_numberOfSeasons(link)
                number_seasons = int(seasons)
                verificare_2 = 0
                print("Numarul maxim de sezoane este :" + str(number_seasons))
                while verificare_2 == 0:
                    season_input = input("Sezonul : ")
                    if 0 < int(season_input) <= number_seasons:
                        verificare_2 = 1
                        link_episodes = 'https://www.imdb.com' + new_link + season_input
                        number_episodes = request.get_numberOfEpisodes_season(link_episodes)
                        verificare_3 = 0
                        print("Numarul maxim de episoade este :" + str(number_episodes))
                        while verificare_3 == 0:
                            episode_input = input("Episodul : ")
                            if 0 < int(episode_input) <= int(number_episodes):
                                verificare_3 = 1
                                query = title + ' season ' + season_input + ' episode ' + episode_input
                                link_youtube = request.videos_youtube(query)
                                print(query + '  ' + link_youtube)
                                print("====================================")
                                print("Comanda a fost efectuata cu succes !")
                                print("====================================")
                            else:
                                print("Acest episod nu exista,mai incearca !")
                    else:
                        print("Acest sezon nu exista,mai incearca !")
        if verificare_1 == 0:
            print("Acest serial nu se afla in baza de date !")


def print_link_youtube():
    """
       Functia va afisa informatiile din tabela 'youtube',adica titlu,episodul,sezonul si link-ul catre youtube al
       ultimului episod vazut dar si a cautarilor utilizatorului.
       :return : none
    """
    series = database.print_youtube()
    print("")
    for serie in series:
        title = serie[1]
        season = serie[2]
        episode = serie[3]
        link_youtube = serie[4]
        print(str(title) + " , sezonul " + str(season) + " , episodul " + str(episode) + " => Link Youtube:" +
              link_youtube)
    print("")


def notificare():
    """
       Functia va verifica daca exista episoade noi pentru fiecare serial din baza de date.In cazul in care exista,ii va
       afisa un mesaj utilizatorul si anume ca 'Au mai aparut x episoade noi in serialul Y'.
       :return : none
    """
    list_series = database.get_series()
    for serie in list_series:
        title = serie[0]
        current_episodes = int(serie[1])
        link = str(serie[3])
        new_episodes = int(request.get_episodes(link))
        if current_episodes < new_episodes:
            print("")
            print("=======================================================================")
            print("Au mai aparut " + str(new_episodes - current_episodes) + " episoade noi in serialul " + str(title))
            print("=======================================================================")
            # database.update_episodes(title,new_episodes)
        elif new_episodes == 0:
            print("Nu s-a putut face request de la IMDB")
