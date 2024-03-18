import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)

mycursor = db.cursor()
mycursor.execute("DELETE from database2.table2 WHERE IDnumber=41")
db.commit()
db.close()