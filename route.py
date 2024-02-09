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
    return render_template("calendario.html")

@app.route("/calendario/visualizza")
def visualizza_calendario():
    query = "SELECT * FROM shows WHERE type = 'TV Show'"
    # items = execute_query(query)
    # return items

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

    return render_template("classifica.html", classifica=classifica)

@app.route("/calciatori")
def calciatori():
    return render_template("calciatori.html")

if __name__ == '__main__':
    app.run(debug=True)