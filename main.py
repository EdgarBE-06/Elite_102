import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring

#top = Tk()

#top.geometry("100x100")
#def show():
   #global name
  # name = askstring("Input", "Enter your name")
  # global password
  # password = askstring("Input", "Enter your password")
  # print(name, password)
   
   
#B = Button(top, text ="Click", command = show)
#B.place(x=50,y=50)

#top.mainloop()

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)



def main():
      login()
      choice = input("What would you like to do \n 1.Delete my account \n 2.Check acccount Balance \n 3.Make a Withdrawl \n 4.Make a Deposit \n 5.Modify Account")
      
      if choice == '1':
          print("delete")
          delete_account()
      elif choice == '2':
          print("check")
          check_balance()
      elif choice == '3':
          print("Withdrawl")
          Withdrawl()
      elif choice == '4':
          print('Deposit')
          Deposit()
      elif choice == '5':
          print("Modify")
          Modifying_account()
      else:
        print("Table")
        table()

def login():
    choice = input("1.Login \n2.Create an account")
    
    if choice == '1':
        global name
        name = input("Enter your name ")
        global password
        password = input("Enter your password ")
    elif choice == '2':
       create_account()
    else:
        table()



def table():
    cursor = connection.cursor()
    testQuery = ("SELECT * FROM user_account")
    cursor.execute(testQuery)

    for item in cursor:
       print(item)

    cursor.close()
    
def check_balance():
    cursor = connection.cursor()
    testQuery = (f"SELECT balance FROM user_account WHERE name = '{name}' and password = '{password}")
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
   cursor = connection.cursor()
   addData = (f"DELETE FROM user_account WHERE name = '{name}' and password = '{password}'")
   cursor.execute(addData)

   connection.commit()
   cursor.close()
   
def Deposit():
      cursor = connection.cursor()
      deposit_amount = int(input("How much would you like to deposit"))
      deposit = (f"UPDATE user_account SET balance = balance + {deposit_amount} WHERE name = '{name}';")
      cursor.execute(deposit)

      connection.commit()
      cursor.close()
   
def Withdrawl():
      cursor = connection.cursor()
      withdrawl_amount = int(input("How much would you like to withdrawl"))
      withdrawl = (f"UPDATE user_account SET balance = balance - {withdrawl_amount} WHERE name = '{name}';")
      cursor.execute(withdrawl)

      connection.commit()
      cursor.close()
      
def Modifying_account():
    cursor = connection.cursor()
    mod_choice = input("Would you like to change your name, email, or password ")
    if mod_choice == 'name':
        new_name = input("What do you want to change your name to ")
        name_change = (f"UPDATE user_account SET name = '{new_name}' WHERE name = '{name}'")
        cursor.execute(name_change)

        connection.commit()
        cursor.close()

    elif mod_choice == 'email':
        new_email = input("What's your new email ")
        email_change = (f"UPDATE user_account SET email = '{new_email}' WHERE name = '{name}'")
        cursor.execute(email_change)

        connection.commit()
        cursor.close()

    elif mod_choice == 'password':
        new_password = input("Please enter your new password ")
        password_change = (f"UPDATE user_account SET password = '{new_password}' WHERE name = '{name}'")
        cursor.execute(password_change)

        connection.commit()
        cursor.close()
    else:
        Modifying_account()

main()