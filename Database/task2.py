# Ask the user to enter a number. Once the user enters the number, fetch the rows corresponding to the number entered by the user and display the data in the proper format

import mysql.connector
connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='python'
    )

cursor = connection.cursor(dictionary=True)
query = 'SELECT * FROM users ORDER BY id ASC'
cursor.execute(query)

while True:
    rows = input('How many number of rows you whould like to fetch : ')
    users = cursor.fetchmany(int(rows))
    if not len(users):
        break
    for user in users:
        print(
            f'''
              Name => {user['name']}
              Phone => {user['phone']}
              Email => {user['email']}
              
            ''')