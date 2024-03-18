import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password",
    database="database2"
)

mycursor = db.cursor()
# previously it was 40 now it is 41
mycursor.execute("SELECT * FROM table2")
ans = mycursor.fetchall()
for i in ans:
    print(i)
db.commit()
db.close()