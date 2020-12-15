import commands
import threading
import time


def task1():
    """
        Acest thread va fi folosit pentru verificarea inputului primit de utilizator. In cazul in care se potriveste
        cu o comanda anume,o va executa.
        :return : none
    """
    time.sleep(1)
    ok = 1
    while ok == 1:
        print("Comenzile existente sunt :")
        print("                          Adaugare serial")
        print("                          Stergere serial")
        print("                          Modificare scor")
        print("                          snooze/unsnooze")
        print("                          Listare")
        print("                          Modificare episod")
        print("                          youtube")

        comanda = input("Introdu Comanda : ")

        if comanda.find("Adaugare serial") != -1:
            link = input("Introdu link : ")
            commands.adaugare_serial(link)
        elif comanda.find("Listare") != -1:
            commands.listare()
            ok = 0
        elif comanda.find("Stergere serial") != -1:
            commands.delete_serie()
        elif comanda.find("Modificare scor") != -1:
            commands.modify_score()
        elif comanda.find("unsnooze") != -1:
            commands.unsnooze_serie()
        elif comanda.find("snooze") != -1:
            commands.snooze_serie()
        elif comanda.find("Modificare episod") != -1:
            commands.modify_last_episode()
        elif comanda.find("youtube") != -1:
            commands.search_youtube()


def task2():
    """
           Acest thread va face fi folosit pentru notificarea in cazul in care apar episoade noi,dar va afisa si
           link-urile de pe youtube a ultimelor episoade vazute
           :return : none
    """
    commands.print_link_youtube()
    commands.notificare()


t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')

t2.start()
t1.start()

t1.join()
t2.join()

# database.add_serie('Lista neagra', 120, 10, 'https://www.imdb.com/title/tt2741602/?ref_=fn_al_tt_1', 120,
# "2019-12-12-20",0)
# database.add_serie('The crown', 130, 8, 'https://www.imdb.com/title/tt1632701/?ref_=fn_al_tt_1',120,"2019-12-12-20",0)
