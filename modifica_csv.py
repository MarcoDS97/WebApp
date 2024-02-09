import mysql.connector
from mysql.connector import Error
import csv
import random


file = open("Giocatori.csv", mode="r", encoding="utf-8", newline=""):
nuovo_file = open("Giocatori_nuovo.csv", mode="x", encoding="utf-8", newline="")

lettore = csv.reader(file, delimiter=";")
scrittore = csv.reader(nuovo_file, delimiter=";")

next(lettore)

# N. maglia --> creare set con 99 numeri e fare .pop()
# Età --> random number in range 18-35
# ruolo --> lista con 4 elementi, dove il portiere è 1 random range(2-12) //3 per decidere gli altri ruoli 10% portiere, 30% altri ruoli




for riga in lettore:
    print(riga)

nuovo_file.close()
file.close()



