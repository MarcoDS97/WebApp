import csv
from funzioni_connessioni import *

# query_giocatori = """
#     CREATE TABLE IF NOT EXISTS giocatori(
#     id_giocatore INT(11) PRIMARY KEY AUTO_INCREMENT,
#     nome VARCHAR(255),
#     cognome VARCHAR(255),
#     nazionalita VARCHAR(255),
#     ruolo VARCHAR(255),
#     numero_maglia INT(11),
#     eta INT(11),
#     id_squadra INT(11)
#     );
#     """
# execute_query_insert(query_giocatori)
#
# try:
#     fk_giocatori = """
#         ALTER TABLE giocatori
#         ADD CONSTRAINT fk_squadra FOREIGN KEY (id_squadra) REFERENCES squadra(id_squadra)
#         """
#     execute_query_insert(fk_giocatori)
# except:
#     pass

#prendere tutte le squadre
set_squadre = set()
with open("gestione_giocatori/Giocatori_completato.csv", "r", encoding="utf-8") as file_per_set:
    lettore = csv.reader(file_per_set, delimiter=";")
    next(lettore)
    for riga in lettore:
        set_squadre.add(riga[3])
print(set_squadre)
diz_squadre = {}
count= 1
for elem in set_squadre:
    diz_squadre.update({elem: count})
    count += 1

print(diz_squadre)

query_inserimento = (
    "INSERT INTO giocatori (nome, cognome, nazionalita, id_squadra, ruolo, numero_maglia, eta) " 
    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
)

# file = open("gestione_giocatori/Giocatori_test.csv", mode="r", encoding="utf-8", newline="")
#
# lettore = csv.reader(file, delimiter=";")
#
# next(lettore)

# for riga in lettore:
#
#     execute_query_insert(
#         query_inserimento,
#         (
#             riga[0],
#             riga[1],
#             riga[2],
#             diz_squadre[riga[3]],
#             riga[4],
#             riga[5],
#             riga[6]
#
#         ))
#
#