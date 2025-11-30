import mysql.connector
connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='python')
cursor = connection.cursor()
id = input("Please enter user id for update email : ")
email = input("Please enter your new email : ")
query = 'UPDATE users SET email = %s WHERE id = %s'
cursor.execute(query, (email, id ))
print('Your email has been updated')
connection.commit()