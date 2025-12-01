### Connect with database

## For mysql use this package
# - pip install mysql-connector-python
import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='python')
print(connection.is_connected())
cursor = connection.cursor(dictionary=True)

# Pass "dictionary=True" in cursor to get data in key value pair 

name = input('Please Enter your name to check your id : - ')
query = "SELECT * FROM USERS WHERE id = %s"
# query = f"SELECT id, name FROM USERS WHERE email =  '{email}'"
# print(query, )
#this is how we can pass perameters in a query
cursor.execute(query, (name,))
users = cursor.fetchall()
print(users[0]['name'])

# print(cursor.fetchall()) # for fetching all data
# print(cursor.fetchone()) # for fetching one line
# print(cursor.fetchmany(3)) # This will fetch first 3 records and calling again will fetch next 3 records



## For pgsql use this package 
# pip install psycopg2-binary
# import psycopg2
