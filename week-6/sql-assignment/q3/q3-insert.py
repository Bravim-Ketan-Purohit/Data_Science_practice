import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)
mycursor = db.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS database2')
mycursor.execute('CREATE table IF NOT EXISTS database2.table2(name VARCHAR(40),IDnumber INT)')
mycursor.execute('INSERT INTO database2.table2 values("bravim",148)')
mycursor.execute('INSERT INTO database2.table2 values("sparsh",145)')
mycursor.execute('INSERT INTO database2.table2 values("swayam",40)')
db.commit()
db.close()