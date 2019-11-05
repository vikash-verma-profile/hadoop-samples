import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Mindz@007",
  database="trainingdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)