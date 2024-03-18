import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)

mycursor = db.cursor()
# previously it was 40 now it is 41
mycursor.execute("UPDATE database2.table2 SET IDnumber=041 WHERE name='swayam'")
db.commit()
db.close()