
import commands


print("Comenzile existente sunt :")
print("                          Adaugare serial")
print("                          Stergere serial")
print("                          Modificare scor")
print("                          snooze/unsnooze")
print("                          Listare")

comanda = input("Introdu Comanda : ")

if comanda.find("Adaugare serial") != -1:
    link = input("Introdu link : ")
    scor = input("Introdu scor : ")
    commands.adaugare_serial(link, scor)
elif comanda.find("Listare") != -1:
    commands.listare()
elif comanda.find("Stergere serial") != -1:
    title = input("Ce serial vrei sa stergi ? : ")
    commands.delete_serie(title)
elif comanda.find("Modificare scor") != -1:
    title = input("Ce serial vrei sa modifici ? : ")
    score = input("Introdu scor : ")
    commands.modify_score(title, score)
elif comanda.find("unsnooze") != -1:
    title = input("Ce serial vrei sa pui pe unsnooze ? : ")
    commands.unsnooze_serie(title)
elif comanda.find("snooze") != -1:
    title = input("Ce serial vrei sa pui pe snooze ? : ")
    commands.snooze_serie(title)

