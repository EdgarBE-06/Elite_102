import mysql.connector

def welcome_message():
    name = input("Hey there sport what's your name?")
    print(f"Hi {name} how's your day been")

welcome_message()

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM user_account")
cursor.execute(testQuery)

for item in cursor:
    print(item)

cursor.close()
connection.close()