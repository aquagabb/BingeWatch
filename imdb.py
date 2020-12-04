import requests
import re


def get_informations(movie):
    if movie.find('https:') != -1:
        serial_url = movie
    else:
        print("HELOO")
        serial_url = "https://www.imdb.com/title/" + movie + "/"
    r = requests.get(url=serial_url)
    # getTitle
    search_title = 'meta name="title" content='
    result = re.search(search_title, r.text)
    nume_titlu = result.string[result.end()+1:result.end()+50]
    index1 = nume_titlu.find('(')
    nume_titlu = nume_titlu[0:index1]
    # getEpisodes
    search_episodes = 'span class="bp_sub_heading">'
    result_episodes = re.search(search_episodes, r.text)
    episoade = result_episodes.string[result_episodes.end():result_episodes.end()+15]
    index_episodes = episoade.find('episodes')
    episoade = episoade[0:index_episodes-1]

    return nume_titlu, episoade


id_movie = input()

titlu, episoade_curente = get_informations(id_movie.replace(" ",""))
print(titlu)
print(episoade_curente)
