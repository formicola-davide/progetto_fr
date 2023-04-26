import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS F1")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS F1.Piloti (
    Cognome VARCHAR(30) NOT NULL,
    Nome VARCHAR(30),
    Nazionalità VARCHAR(30),
    Numero INTEGER(30),
    Scuderia VARCHAR(30),
    Età INTEGER(30),
    Pole_Position INTEGER(30),
    Podi INTEGER(30),
    Vittorie INTEGER(30),
    PRIMARY KEY (Cognome)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM F1.Piloti")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./piloti.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO CLASH_ROYALE.Clash_Unit VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * F1.Piloti")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)