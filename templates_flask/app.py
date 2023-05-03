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
def unitList():
    mycursor.execute("SELECT * FROM Piloti")
    myresult = mycursor.fetchall()
    return render_template('piloti.html', Cognome=myresult)
