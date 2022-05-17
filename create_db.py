import mysql.connector

my = mysql.connector.connect(
    host="localhost",
    user="kimberly",
    passwd="kim12345",
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE our_users")

my_cursor.execute("SHOW DATABASE")
for db in my_cursor:
    print(db)