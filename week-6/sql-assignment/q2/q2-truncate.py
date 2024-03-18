# 3 --> truncate
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
mycur = mydb.cursor()
mycur.execute("insert into database1.table1 values('hello',99,99.9925)")
mycur.execute("insert into database1.table1 values('hello',99,99.9925)")
mycur.execute("insert into database1.table1 values('hello',99,99.9925)")
mycur.execute("insert into database1.table1 values('hello',99,99.9925)")
mycur.execute("insert into database1.table1 values('hello',99,99.9925)")
# adding data for the execution of truncate
mycur.execute("TRUNCATE TABLE database1.table1")


mydb.commit()
mydb.close()