import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="Student")

mycursor = mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
    print(i)

mycursor.execute("select * from studentRegistar")
for i in mycursor:
    print(i)
