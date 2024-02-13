
import json
import mysql.connector
from funzioni_connessioni import *
from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def homepage():
    # """SELECT SUM(gs1) AS "Gol subiti", SUM(gs2) AS "Gol fatti"
    # FROM risultati INNER JOIN squadra
    # ON risultati.id_s2 = squadra.id_squadra
    # WHERE id_s2 = %s"""        fuori-casa

    # """SELECT SUM(gs1) AS "Gol fatti", SUM(gs2) AS "Gol subiti"
    # FROM risultati INNER JOIN squadra
    # ON risultati.id_s1 = squadra.id_squadra
    # WHERE id_s1 = %s"""        in-casa

    query_squadre = "SELECT nome FROM squadra"
    diz_squad = execute_query(query_squadre)
    lista_squad = []
    for elem in diz_squad:
        lista_squad.append(elem["nome"])

    gol_1 = []
    gol_2 = []
    for squadra in lista_squad:
        query1 = f"""SELECT SUM(gs1) AS "Gol subiti", SUM(gs2) AS "Gol fatti", squadra.nome
        FROM risultati INNER JOIN squadra
        ON risultati.id_s2 = squadra.id_squadra
        WHERE squadra.nome = %s"""
        risultato = execute_query(query1, (squadra,))
        if risultato[0]["nome"] == None:
            risultato = [{"Gol subiti":0, "Gol fatti":0, "nome":squadra}]
        gol_1.append(risultato[0])
        query2 = f"""SELECT SUM(gs1) AS "Gol fatti", SUM(gs2) AS "Gol subiti", squadra.nome
        FROM risultati INNER JOIN squadra
        ON risultati.id_s1 = squadra.id_squadra
        WHERE squadra.nome = %s"""
        risultato = execute_query(query2, (squadra,))
        if risultato[0]["nome"] == None:
            risultato = [{"Gol subiti":0, "Gol fatti":0, "nome":squadra}]
        gol_2.append(risultato[0])

    for elem in gol_1:
        for elem2 in gol_2:
            if elem["nome"] == elem2["nome"]:
                elem["Gol fatti"] += elem2["Gol fatti"]
                elem["Gol subiti"] += elem2["Gol subiti"]
                elem["Differenza reti"] = elem["Gol fatti"] - elem["Gol subiti"]

    immagini = ["./static/Img/Atalanta.png", "./static/Img/Bologna.png", "./static/Img/Cagliari.png", "./static/Img/Empoli.png",
                "./static/Img/Fiorentina.png", "./static/Img/Fiorentina.png", "./static/Img/Frosinone.png", "./static/Img/Genoa.png",
                "./static/Img/Inter.png", "./static/Img/Juventus.png", "./static/Img/Lazio.png", "./static/Img/Lecce.png",
                "./static/Img/Milan.png", "./static/Img/Monza.png", "./static/Img/Napoli.png", "./static/Img/Roma.png",
                "./static/Img/Salernitana.png", "./static/Img/Sassuolo.png", "./static/Img/Torino.png", "./static/Img/Udinese.png",
                "./static/Img/Verona.png"]
    return render_template("home.html", lista_squadre=gol_1, immagini=immagini)

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

    query = """
        SELECT *
        FROM squadra
    """ 

    id_nome_squadra = execute_query(query)

    return render_template("calciatori.html", diz_squadra=diz_squadra, numero_squadre=numero_squadre, id_nome_squadra=id_nome_squadra)


@app.route("/form_ins_sqd", methods=["GET", "POST"])
def form_ins_sqd():
    if request.method == "POST":
        numero_squadre = int(request.form["numero_squadre"])
        return redirect(url_for("inserisci_nomi_squadre", numero_squadre=numero_squadre))
    return render_template("form_inserimento_numero_squadre.html")

@app.route("/inserisci_nomi_squadre/<int:numero_squadre>", methods=["GET", "POST"])
def inserisci_nomi_squadre(numero_squadre):
    if request.method == "POST":
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        for i in range(numero_squadre):
            nome_squadra = request.form[f"squadra_{i}"]
            cursor.execute("INSERT INTO squadra (nome) VALUES (%s)", (nome_squadra,))
        
        conn.commit()
        conn.close()

        return "Dati inseriti correttamente! <a href='/'>Torna alla Home</a>"
        

    return render_template("form_inserimento_nomi_squadre.html", numero_squadre=numero_squadre)



@app.route("/calciatori/inserisci_giocatore", methods=['POST'])
def inserisci_giocatore():
    giocatore = [
        request.form.get('Nome'),
        request.form.get('Cognome'),
        request.form.get('Nazionalità'),
        request.form.get('j'),
        request.form.get('Ruolo'),
        request.form.get('Numero maglia'),
        request.form.get('Età')
    ]

    query_inserimento = (
    "INSERT INTO giocatori (nome, cognome, nazionalita, id_squadra, ruolo, numero_maglia, eta) " 
    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )

    execute_query_insert(query_inserimento, giocatore)
    
    return redirect(url_for("calciatori", _anchor=request.form.get('j')))


if __name__ == '__main__':
    app.run(debug=True)