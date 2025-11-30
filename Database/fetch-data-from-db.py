### Connect with database

## For mysql use this package
# - pip install mysql-connector-python
import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='python')
print(connection.is_connected())
cursor = connection.cursor()

name = input('Please Enter your name to check your id : - ')
email = input(f'Hey {name} Please Enter your registered email to check details : - ')
query = "SELECT * FROM USERS WHERE email = %s AND name = %s"
# query = f"SELECT id, name FROM USERS WHERE email =  '{email}'"
print(query, )
#this is how we can pass perameters in a query
cursor.execute(query, (email, name))
users = cursor.fetchall()
print(users )

# print(cursor.fetchall()) # for fetching all data
# print(cursor.fetchone()) # for fetching one line



## For pgsql use this package 
# pip install psycopg2-binary
# import psycopg2
