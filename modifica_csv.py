import mysql.connector
from mysql.connector import Error
import csv
from faker import Faker


file = open("Giocatori.csv", mode="r", encoding="utf-8", newline=""):
nuovo_file = open("Giocatori_nuovo.csv", mode="x", encoding="utf-8", newline="")

lettore = csv.reader(file, delimiter=";")
scrittore = csv.reader(nuovo_file, delimiter=";")

next(lettore)

for riga in lettore:
    print(riga)

nuovo_file.close()
file.close()

