import requests
import re


def get_informations(movie):
    """
           Face request la link-ul primit,va returna titlu si numarul de episoade
           specific serialului de la link-ul respectiv.
           :param movie : Primeste ca parametrul link-ul de la IMDB
           :return : nume_titlu,episoade
    """
    if movie.find('https:') != -1:
        serial_url = movie
    else:
        serial_url = "https://www.imdb.com/title/" + movie + "/"
    r = requests.get(url=serial_url)
    if r.status_code == 200:
        # getTitle
        search_title = 'meta name="title" content='
        result = re.search(search_title, r.text)
        nume_titlu = result.string[result.end() + 1:result.end() + 50]
        index_titlu = nume_titlu.find('(')
        nume_titlu = nume_titlu[0:index_titlu - 1]
        # getEpisodes
        search_episodes = 'span class="bp_sub_heading">'
        result_episodes = re.search(search_episodes, r.text)
        episoade = result_episodes.string[result_episodes.end():result_episodes.end() + 15]
        index_episodes = episoade.find('episodes')
        episoade = episoade[0:index_episodes - 1]
        return nume_titlu, episoade
    elif r.status_code == 404:
        return "", ""


def get_episodes(link):
    """
        Face request la link-ul primit si va cauta numarul de episoade specific serialului
        :param link : Primeste ca parametrul link-ul de la IMDB
        :return : episoade
    """
    if link.find('https:') != -1:
        serial_url = link
    else:
        serial_url = "https://www.imdb.com/title/" + link + "/"
    r = requests.get(url=serial_url)

    if r.status_code == 200:
        search_episodes = 'span class="bp_sub_heading">'
        result_episodes = re.search(search_episodes, r.text)
        episoade = result_episodes.string[result_episodes.end():result_episodes.end() + 15]
        index_episodes = episoade.find('episodes')
        episoade = episoade[0:index_episodes - 1]
        return episoade
    elif r.status_code == 404:
        episoade = 0
        print("EROR 404")
        return episoade


def get_numberOfSeasons(link):
    """
    Face request la link-ul primit si va cauta numarul de sezoane specific serialului dar si
    link-ul dupa care se va putea lua numarul de episoade din fiecare sezon.
    :param link : Primeste ca parametrul link-ul de la IMDB
    :return : number_of_seasons,link_request_season
    """
    if link.find('https:') != -1:
        serial_url = link
    else:
        serial_url = "https://www.imdb.com/title/" + link + "/"
    r = requests.get(url=serial_url)
    if r.status_code == 200:
        search_seasons = '<br class="clear" />'
        result_seasons = re.search(search_seasons, r.text)
        number_of_seasons = result_seasons.string[result_seasons.end() + 80:result_seasons.end() + 115]
        link_request_season = result_seasons.string[result_seasons.end() + 80:result_seasons.end() + 113]
        index_episodes = number_of_seasons.find('season=')
        seasons_variable = number_of_seasons[index_episodes + 7:index_episodes + 9]
        index_seasons = seasons_variable.find('"')
        if index_seasons != -1:
            number_of_seasons = seasons_variable[0:index_seasons]
        return number_of_seasons, link_request_season
    elif r.status_code == 404:
        number_of_seasons = 0
        link_request_season = ""
        return number_of_seasons, link_request_season


def get_numberOfEpisodes_season(link):
    """
    Functia face request la link-ul primit si va cauta numarul de episoade specific sezonului
    :param link : Primeste ca parametrul link-ul de la IMDB
    :return : number_of_episodes
    """
    r = requests.get(url=link)
    if r.status_code == 200:
        search_episodes = 'itemprop="numberofEpisodes" content="'
        result_episodes = re.search(search_episodes, r.text)
        number_of_episodes = result_episodes.string[result_episodes.end():result_episodes.end() + 4]
        index_seasons = number_of_episodes.find('"')
        if index_seasons != -1:
            number_of_episodes = number_of_episodes[0:index_seasons]
        return number_of_episodes
    elif r.status_code == 404:
        number_of_episodes = 0
        return number_of_episodes


def videos_youtube(query):
    """
     Va face request la youtube folosind acest query.Va cauta link-ul catre primul episod de pe youtube.
     :param query : Primeste ca parametrul un string dat de utilizator de tipul "Titlu season x episode y"
     :return : link_youtube
    """
    query = query.strip().replace(" ", "+")
    serial_url = 'https://www.youtube.com/results?search_query=' + query
    r = requests.get(url=serial_url)
    if r.status_code == 200:
        videos_id = '"videoRenderer":{"videoId":"'
        result_episodes = re.search(videos_id, r.text)
        video = result_episodes.string[result_episodes.end():result_episodes.end() + 11]
        link_youtube = 'https://www.youtube.com/watch?v=' + video
        return link_youtube
    elif r.status_code == 404:
        link_youtube = ''
        return link_youtube
