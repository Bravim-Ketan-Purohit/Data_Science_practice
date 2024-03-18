# 2 --> Alter
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
mycur = mydb.cursor()
mycur.execute("DROP TABLE if exists database1.table1")
mydb.commit()
mydb.close()