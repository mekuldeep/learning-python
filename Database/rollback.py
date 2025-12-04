# rollback is maybe use for revert the query import mysql.connector

connection = mysql.connector.connect(...)

with connection.cursor() as cursor:
    try:
        cursor.execute("INSERT INTO test (name) VALUES ('A')")
        cursor.execute("INSERT INTO test (name) VALUES ('B')")
        connection.commit()
    except:
        connection.rollback()



# hat is a Transaction?./3

# A transaction is a group of SQL operations that are exe