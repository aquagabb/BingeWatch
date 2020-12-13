import commands
import threading
import time


def task1():
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

        # database.add_serie('Costume', 120, 10, 'https://www.imdb.com/title/tt1632701/?ref_=fn_al_tt_1', 120,
        # datetime.now(), 0)

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
    commands.print_link_youtube()
    commands.notificare()


t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')

# starting threads
t2.start()
t1.start()
# wait until all threads finish
t1.join()
t2.join()
