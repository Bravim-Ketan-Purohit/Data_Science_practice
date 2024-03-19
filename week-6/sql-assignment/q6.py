import mysql.connector

# this is used to connect to database
db = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)

# Cursor is a Temporary Memory or Temporary Work Station. It is Allocated by Database Server at the Time of Performing DML(Data Manipulation Language) operations on the Table by the User. Cursors are used to store Database Tables. 
# There are 2 types of Cursors: Implicit Cursors, and Explicit Cursors. These are explained as following below.
# Implicit Cursors: Implicit Cursors are also known as Default Cursors of SQL SERVER. These Cursors are allocated by SQL SERVER when the user performs DML operations.
# Explicit Cursors: Explicit Cursors are Created by Users whenever the user requires them. Explicit Cursors are used for Fetching data from Table in Row-By-Row Manner.
mycursor = db.cursor()

# execute is used for executing sql query within from programming language
mycursor.execute('CREATE DATABASE IF NOT EXISTS database2')
db.commit()
db.close()