import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Mindz@007",
  database="trainingdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM login")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)