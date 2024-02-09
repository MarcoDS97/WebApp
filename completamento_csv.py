import random


file = open("Giocatori.csv", mode="r", encoding="utf-8", newline="")
nuovo_file = open("Giocatori_completato.csv", mode="w", encoding="utf-8", newline="")


nuovo_file.write("NOME;COGNOME;NAZIONE;SQUADRA;RUOLO;MAGLIA;ETA\n")
file.readline()

#generazione lista di  99 numeri unici in ordine casuale
lista_maglie =  []
set_maglie = set()
while len(set_maglie) < 99: 
    num = random.randint(1,99)

    if num not in set_maglie:
        lista_maglie.append(num)
        set_maglie.add(num)


for riga in file.readlines():

    nuova_stringa = ""

    # Ruolo --> range casuale (2-11) // 3, indice 0 (il portiere) ha 10% di probabiltà di uscire, gli altri 30%
    lista_ruoli = ["Portiere", "Difensore", "Centrocampista", "Attaccante"]
    nuova_stringa += ";" + lista_ruoli[random.randint(2,11)//3] + ";"

    # N. maglia --> pop() casuale da una lista di 99 numeri
    nuova_stringa += str(lista_maglie.pop()) + ";"

    # Età --> numero random in range 18-35
    nuova_stringa += str(random.randint(18,36)) + ";" + "\n"

    #separo nome e cognome, eccezione per nome senza cognome
    try:
        stringa_csv = riga[:riga.index(" ")] + ";" + riga[riga.index(" ") + 1:].strip()
    except:
        stringa_csv = riga.strip()

    nuovo_file.write(stringa_csv + nuova_stringa)


nuovo_file.close()
file.close()

