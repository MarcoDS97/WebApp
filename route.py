import json
import mysql.connector
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/calendario")
def calendario():
    return render_template("calendario.html")

@app.route("/classifica")
def classifica():
    return render_template("classifica.html")

@app.route("/calciatori")
def calciatori():
    return render_template("calciatori.html")

if __name__ == '__main__':
    app.run(debug=True)