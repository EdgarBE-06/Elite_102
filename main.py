import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)

def welcome_message():
    name = input("What's your name?")
    cursor = connection.cursor()
    testQuery = ("SELECT * FROM user_account WHERE balance > 50")
    cursor.execute(testQuery)

    for item in cursor:
       print(item)

    cursor.close()
    connection.close()

welcome_message()