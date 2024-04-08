import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)



def main():
    choice = input("What would you like to do")
    if choice == 'create an account':
        create_account()
    elif choice == 'delete my account':
        delete_account()
    elif choice == 'check my balance':
        check_balance()
    elif choice == 'make a deposit':
        Deposit()
    elif choice == 'make a withdrawl':
        Withdrawl()
    elif choice == 'modify my account':
        Modifying_account()
    else:
        main()


def table():
    cursor = connection.cursor()
    testQuery = ("SELECT * FROM user_account")
    cursor.execute(testQuery)

    for item in cursor:
       print(item)

    cursor.close()
    
def check_balance():
    cname = input("What's your name ")
    cursor = connection.cursor()
    testQuery = (f"SELECT balance FROM user_account WHERE name = '{cname}' ")
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
      
def Modifying_account():
    mod_name = input("What's your name ")
    cursor = connection.cursor()
    mod_choice = input("Would you like to change your name, email, or password ")
    if mod_choice == 'name':
        new_name = input("What do you want to change your name to ")
        name_change = (f"UPDATE user_account SET name = '{new_name}' WHERE name = '{mod_name}'")
        cursor.execute(name_change)

        connection.commit()
        cursor.close()

    elif mod_choice == 'email':
        new_email = input("What's your new email ")
        email_change = (f"UPDATE user_account SET email = '{new_email}' WHERE name = '{mod_name}'")
        cursor.execute(email_change)

        connection.commit()
        cursor.close()

    elif mod_choice == 'password':
        new_password = input("Please enter your new password ")
        password_change = (f"UPDATE user_account SET password = '{new_password}' WHERE name = '{mod_name}'")
        cursor.execute(password_change)

        connection.commit()
        cursor.close()
    else:
        Modifying_account()

main()
table()