import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)

def main():
    cursor = connection.cursor()
    testQuery = ("SELECT * FROM user_account")
    cursor.execute(testQuery)

    for item in cursor:
       print(item)

    cursor.close()
    connection.close()
    
def create_account():
   aname = input("What's your name ")
   aemail = input("What's your email ")
   apassword = input("What's your password ")
   abalance = 0
   cursor2 = connection.cursor()
   addData = (f"INSERT INTO user_account (name, email, password, balance)VALUES ('{aname}','{aemail}','{apassword}', {abalance})")
   cursor2.execute(addData)

   connection.commit()
   cursor2.close()
   connection.close()

def delete_account():
   dname = input("What is the name of your account")
   cursor3 = connection.cursor()
   addData = ("DELETE FROM user_account")
   cursor3.execute(addData)

   connection.commit()
   cursor3.close()
   connection.close()

create_account()