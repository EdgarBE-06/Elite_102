import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)

def table():
    cursor = connection.cursor()
    testQuery = ("SELECT * FROM user_account")
    cursor.execute(testQuery)

    for item in cursor:
       print(item)

    cursor.close()
    
    
def create_account():
   aname = input("What's your name ")
   aemail = input("What's your email ")
   apassword = input("What's your password ")
   abalance = 0
   cursor = connection.cursor()
   addData = (f"INSERT INTO user_account (name, email, password, balance)VALUES ('{aname}','{aemail}','{apassword}', {abalance})")
   cursor.execute(addData)

   connection.commit()
   cursor.close()
   

def delete_account():
   dname = input("What's your name ")
   cursor = connection.cursor()
   addData = (f"DELETE FROM user_account WHERE name = '{dname}'")
   cursor.execute(addData)

   connection.commit()
   cursor.close()
   

def Deposit():
      depo_name = input("What's your name ")
      cursor = connection.cursor()
      deposit_amount = int(input("How much would you like to deposit"))
      deposit = (f"UPDATE user_account SET balance = balance + {deposit_amount} WHERE name = '{depo_name}';")
      cursor.execute(deposit)

      connection.commit()
      cursor.close()
   

def Withdrawl():
      with_name = input("What's your name ")
      cursor = connection.cursor()
      withdrawl_amount = int(input("How much would you like to withdrawl"))
      withdrawl = (f"UPDATE user_account SET balance = balance - {withdrawl_amount} WHERE name = '{with_name}';")
      cursor.execute(withdrawl)

      connection.commit()
      cursor.close()
      

   

   
