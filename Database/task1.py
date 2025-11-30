# Ask user to enter name, email and mobile number and then save details on DB validate the email

import mysql.connector
connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='python')
cursor = connection.cursor()
print('Please enter the details to register')
name = input('Please enter your name : ')
email = input(f'Hey {name}, please enter your email : ')

while not email.endswith('@gmail.com'):
    print('Please enter a vaild email (gmail.com only)')
    email = input('Please enter your email : ')

number = input('Please enter your number : ')
while len(number) < 10 or len(number) > 15:
    print('Please enter a valid number, It should be between 10-15')
    number = input('Please enter your number : ')
    
query = 'INSERT INTO users (name, phone, email) VALUES( %s, %s, %s )'
cursor.execute(query, (name, email, number))

print(
    f'''
    ----------------------------------------------------------------------------------
    
                Thank you, please verify your details and press Enter for submit
                    Name = { name }
                    Email = { email }
                    Number = { number }
      
    ----------------------------------------------------------------------------------
      ''')

input()
connection.commit() 

    