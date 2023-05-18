from flask import render_template
from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="F1"
)
mycursor = mydb.cursor()

app = Flask(__name__)


@app.route('/Cognome')
def pilotList():
    mycursor.execute("SELECT * FROM Piloti")
    myresult = mycursor.fetchall()
    return render_template('piloti.html', tabella_piloti=myresult)


@app.route('/Cognome/<pilota>')
def pilot(pilota):
    mycursor.execute("SELECT * FROM Piloti where Cognome='{}'".format(pilota))
    myresult = mycursor.fetchall()
    return render_template('cognome.html', tabella_piloti=myresult)
