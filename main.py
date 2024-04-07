import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)

def main():
    cd = input("Would you like to create or delete an account")
    if cd == 'create':
       create_account()
    elif cd == 'delete':
       delete_account()
    else:
       print("That's not an option")

    cursor = connection.cursor()
    testQuery = ("SELECT * FROM user_account")
    cursor.execute(testQuery)

    for item in cursor:
       print(item)

    cursor.close()
    connection.close()
    
def create_account():
   cursor2 = connection.cursor()
   addData = ("INSERT INTO user_account (name, email, password, balance)VALUES ('John','Ree@gmail.com','hoho', 0)")
   cursor2.execute(addData)

   connection.commit()
   cursor2.close()
   connection.close()

def delete_account():
   dname = input("What is the name of your account")
   cursor3 = connection.cursor()
   addData = (f"DELETE FROM user_account WHERE name = {dname}")
   cursor3.execute(addData)

   connection.commit()
   cursor3.close()
   connection.close()

main()