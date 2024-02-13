import csv
import random

lista_nazioni = ["Italia", "Inghilterra", "Francia", "Spagna", "Portogallo", "Germania", "Albania", "Macedonia", "Lussemburgo",
                 "Russia", "Polonia", "Egitto", "Marocco", "Algeria", "Tunisia", "Belgio", "Estonia", "Lettonia", "Lituania"]
with open("Squadre_ita.csv", "r", encoding="utf-8", newline="") as file:
    lettore = csv.reader(file, delimiter=";")
    next(lettore)
    with open("Giocatori_completato.csv", "w", encoding="utf-8", newline="") as nuovo:
        scrittore = csv.writer(nuovo, delimiter=";")
        nuovo.write("Nome;Cognome;Ruolo;Squadra;Maglia;Eta;Nazione\n")
        for riga in lettore:
            print(riga)
            eta = random.randint(18,36)
            naz = random.randint(0, len(lista_nazioni)-1)
            nome = riga[3].split(" ", 1)
            try:
                cognome = nome[1]
            except:
                cognome = ""
            print(nome[0], cognome, eta, lista_nazioni[naz])
            nuovo.write(f"{nome[0]};{cognome};{riga[2]};{riga[0]};{riga[1]};{eta};{lista_nazioni[naz]}\n")