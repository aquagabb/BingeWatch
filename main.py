import database
import datetime



title = input("Numele serialului: ")
episodes = 35
score = 7
linkImdb = "imd12312"
lastEpisode = 25
lastView = datetime.datetime.now()
snooze = 0

database.createTable()
database.addSerie(title, episodes, score, linkImdb, lastEpisode, lastView, snooze)
database.printSeries()
