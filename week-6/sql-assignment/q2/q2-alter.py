# 2 --> Alter
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
mycur = mydb.cursor()
mycur.execute("ALTER TABLE database1.table1 ADD COLUMN col3 FLOAT")
mydb.commit()
mydb.close()