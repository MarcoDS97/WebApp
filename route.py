import json
import mysql.connector
from funzioni_connessioni import *
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/calendario")
def calendario():
    data = visualizza_calendario()


    return render_template("calendario.html", lista_risultati = data)

@app.route("/calendario/visualizza")
def visualizza_calendario():
    query = "SELECT * FROM risultati"
    items = execute_query(query)

    query1 = "SELECT * FROM squadra"
    items1 = execute_query(query1)

    for risultato in items:
        id_s1 = risultato['id_s1']
        id_s2 = risultato['id_s2']

        # Trova i nomi delle squadre utilizzando gli id_squadra
        squadra_s1 = next((squadra['nome'] for squadra in items1 if squadra['id_squadra'] == id_s1), None)
        squadra_s2 = next((squadra['nome'] for squadra in items1 if squadra['id_squadra'] == id_s2), None)

        # Aggiorna il risultato con i nomi delle squadre
        risultato['squadra_s1'] = squadra_s1
        risultato['squadra_s2'] = squadra_s2

    return items

@app.route("/classifica")
def classifica(): #Davide
    query_squadre = "SELECT * FROM squadra"
    squadre = execute_query(query_squadre)
    classifica = []  #conterrà ogni squadra con vittorie, sconfitte e pareggi e verrà ritornato alla fine
    for elem in squadre:
        squadra = {"id": elem["id_squadra"],"nome": elem["nome"],"v":0, "s":0, "p":0, "punteggio":0}
        classifica.append(squadra)

    query_risultati = "SELECT * FROM risultati"
    risultati = execute_query(query_risultati)

    for elem in risultati:      #funzione che calcola vittorie, sconfitte e pareggi dalla tabella risultati
        if elem["gs1"] > elem["gs2"]:
            for squadra in classifica:
                if squadra["id"] == elem["id_s1"]:
                    squadra["v"] += 1
            for squadra in classifica:
                if squadra["id"] == elem["id_s2"]:
                    squadra["s"] += 1

        elif elem["gs1"] == elem["gs2"]:
            for squadra in classifica:
                if squadra["id"] == elem["id_s1"]:
                    squadra["p"] += 1
            for squadra in classifica:
                if squadra["id"] == elem["id_s2"]:
                    squadra["p"] += 1

        elif elem["gs1"] < elem["gs2"]:
            for squadra in classifica:
                if squadra["id"] == elem["id_s1"]:
                    squadra["s"] += 1
            for squadra in classifica:
                if squadra["id"] == elem["id_s2"]:
                    squadra["v"] += 1
    # classifica è una lista di dizionari
    for elem in classifica:
        elem["punteggio"] += (elem["v"]*3 + elem["p"])

    classifica = sorted(classifica, key=lambda x: x["punteggio"], reverse=True)

    return render_template("classifica.html", classifica=classifica)


@app.route("/calciatori")
def calciatori():

    query = """
        SELECT COUNT(DISTINCT id_squadra)
        FROM giocatori
    """ 
    
    numero_squadre = execute_query(query)
    #estrazione valore dal dizionario
    numero_squadre = list(numero_squadre[0].values())[0]

    query = """
        SELECT *
        FROM giocatori
        WHERE id_squadra = %s;
    """
    
    diz_squadra = {}

    for i in range(1,numero_squadre+1):
        diz_squadra[i] = execute_query(query, (i,))

    return render_template("calciatori.html", diz_squadra=diz_squadra, numero_squadre=numero_squadre)


if __name__ == '__main__':
    app.run(debug=True)