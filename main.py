import commands
import imdb
# import threading
#
#
# def task1():
#     ok = 1
#     while ok == 1:
#         print("Comenzile existente sunt :")
#         print("                          Adaugare serial")
#         print("                          Stergere serial")
#         print("                          Modificare scor")
#         print("                          snooze/unsnooze")
#         print("                          Listare")
#
#         # database.add_serie('Costume', 120, 10, 'https://www.imdb.com/title/tt1632701/?ref_=fn_al_tt_1', 120, datetime.now(), 0)
#
#         comanda = input("Introdu Comanda : ")
#
#         if comanda.find("Adaugare serial") != -1:
#             link = input("Introdu link : ")
#             scor = input("Introdu scor : ")
#             commands.adaugare_serial(link, scor)
#         elif comanda.find("Listare") != -1:
#             # commands.listare()
#             commands.get_series()
#             ok = 0
#         elif comanda.find("Stergere serial") != -1:
#             title = input("Ce serial vrei sa stergi ? : ")
#             commands.delete_serie(title)
#         elif comanda.find("Modificare scor") != -1:
#             title = input("Ce serial vrei sa modifici ? : ")
#             score = input("Introdu scor : ")
#             commands.modify_score(title, score)
#         elif comanda.find("unsnooze") != -1:
#             title = input("Ce serial vrei sa pui pe unsnooze ? : ")
#             commands.unsnooze_serie(title)
#         elif comanda.find("snooze") != -1:
#             title = input("Ce serial vrei sa pui pe snooze ? : ")
#             commands.snooze_serie(title)
#
#
# def task2():
#     print("YOUTUBE")
#
#
# t1 = threading.Thread(target=task1, name='t1')
# t2 = threading.Thread(target=task2, name='t2')
#
# # starting threads
# t2.start()
# t1.start()
# # wait until all threads finish
# t1.join()
# t2.join()


commands.seasons_episodes('https://www.imdb.com/title/tt094dasdazs4947/?ref_=tt_sims_tt')

