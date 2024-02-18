import csv
from funzioni_connessioni import *

def inserimento_giocatori():
    
    #prendere tutte le squadre
    set_squadre = set()
    with open("gestione_giocatori/Giocatori_completato.csv", "r", encoding="utf-8") as file_per_set:
        lettore = csv.reader(file_per_set, delimiter=";")
        next(lettore)
        for riga in lettore:
            set_squadre.add(riga[3])
    lista_squad = list(set_squadre)
    lista_squad = sorted(lista_squad)
    diz_squadre = {}
    count= 1
    for elem in lista_squad:
        diz_squadre.update({elem: count})
        count += 1

    #print(diz_squadre)

    lista = [(1, 3, 2, 1, 2, 3),
    (2, 2, 2, 1, 1, 4),
    (3, 0, 1, 2, 2, 1),
    (4, 2, 2, 2, 3, 4),
    (5, 3, 1, 3, 2, 4),
    (6, 2, 2, 3, 3, 1)]
    query_risultati = """INSERT INTO `risultati` (`id_risultato`, `gs1`, `gs2`, `giornata`, `id_s1`, `id_s2`) VALUES
    (%s,%s,%s,%s,%s,%s);"""

    execute_many(query_risultati, lista)

    query_squadre = (
        """INSERT INTO squadra (nome)
        VALUES (%s)"""
    )

    for elem in lista_squad:
        execute_query_insert(query_squadre, (elem,))
    query_inserimento = (
        "INSERT INTO giocatori (nome, cognome, nazionalita, id_squadra, ruolo, numero_maglia, eta) " 
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )

    file = open("gestione_giocatori/Giocatori_completato.csv", mode="r", encoding="utf-8", newline="")

    lettore = csv.reader(file, delimiter=";")

    next(lettore)

    for riga in lettore:

        execute_query_insert(
            query_inserimento,
            (
                riga[0],
                riga[1],
                riga[6],
                diz_squadre[riga[3]],
                riga[2],
                riga[4],
                riga[5]

            ))

