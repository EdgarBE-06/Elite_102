import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)

def welcome_message():
    name = input("What's your name?")
    cursor = connection.cursor()
    testQuery = (f"SELECT * FROM user_account WHERE name = '{name}'")
    cursor.execute(testQuery)

    for item in cursor:
       print(item)

    cursor.close()
    connection.close()

welcome_message()