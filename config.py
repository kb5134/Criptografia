import mysql.connector #pip3 install mysql.connector

#configura o banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="gulosa"
)

