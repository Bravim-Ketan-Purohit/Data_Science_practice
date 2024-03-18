# q2 --> What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.


# DDL stands for Data Definition Language. It is a subset of SQL (Structured Query Language) used to define and manage the structure of a database and its objects. DDL commands are used to create, modify, and delete database objects such as tables, indexes, views, and schemas. Here's an explanation of some common DDL commands and their usage:

# 1 --> create
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)
mycur = mydb.cursor()
mycur.execute("CREATE DATABASE if not exists database1")
mycur.execute("CREATE TABLE if not exists database1.table1(col1 VARCHAR(40),col2 INT);")
mydb.close()

# here a database is created and in that a table is created and two columns namely col1 and col2 are created in that table