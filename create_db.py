import mysql.connector

my = mysql.connector.connect(
    host="localhost",
    user="kimberly",
    passwd="kim12345",
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE test")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)