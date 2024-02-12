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
    return render_template("calendario.html")

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