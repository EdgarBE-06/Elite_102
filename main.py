import mysql.connector
import tkinter
from tkinter import *


window = Tk()


def login():
  window.geometry("400x300")

  label_1 = Label(window, text = "Username")
  label_1.place(x=100,y=75)

  label_2 = Label(window, text = "Password")
  label_2.place(x=100,y=100)

  global name
  name = Entry()
  name.place(x=175, y=75)

  global password
  password = Entry()
  password.place(x=175, y=100)

  btn_1 = Button(window, text = "Login")
  btn_1.place(x=175,y=125)

  btn_2 = Button(window, text = "Sign up", command= lambda: create_account_window())
  btn_2.place(x= 225,y= 125)

  window.mainloop()

def create_account_window():
    second = Toplevel()
    second.title("Sign up page")
    second.geometry("400x300")

    clabel_1 = Label(second, text ="Username")
    clabel_1.place(x=100,y=75)
    abname = Entry(second)
    abname.place(x=175,y=75)

    clabel_2 = Label(second, text ="Email")
    clabel_2.place(x=100,y = 100)
    abemail = Entry(second)
    abemail.place(x=175,y=100)
    
    clabel_3 = Label(second, text="Password")
    clabel_3.place(x=100,y = 125)
    abpassword = Entry(second)
    abpassword.place(x=175,y=125)

    exit_button = Button(second, text="Confirm", command= lambda: create_account(abname, abemail, abpassword)) 
    exit_button.place(x= 175,y= 150) 
  


def create_account(abname, abemail, abpassword):
   aname = abname.get()
   aemail = abemail.get()
   apassword = abpassword.get()
   abalance = 0
   cursor = connection.cursor()
   addData = (f"INSERT INTO user_account (name, email, password, balance)VALUES ('{aname}','{aemail}','{apassword}', {abalance})")
   cursor.execute(addData)

   connection.commit()
   cursor.close()



connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)



def main():
      
      login()
      keep = 'Yes'
      while keep == 'Yes':
        choice = input("What would you like to do \n 1.Delete my account \n 2.Check acccount Balance \n 3.Make a Withdrawl \n 4.Make a Deposit \n 5.Modify Account ")
      
        if choice == '1':
            print("delete")
            delete_account()
            keep = input("Would you like to continue")
        elif choice == '2':
            print("check")
            check_balance()
            keep = input("Would you like to continue")
        elif choice == '3':
            print("Withdrawl")
            Withdrawl()
            keep = input("Would you like to continue")
        elif choice == '4':
            print('Deposit')
            Deposit()
            keep = input("Would you like to continue")
        elif choice == '5':
           print("Modify")
           Modifying_account()
           keep = input("Would you like to continue")
        else:
          print("Table")
          table()
          keep = 'No'
      print("Have a good Day")
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
   
def delete_account():
   cursor = connection.cursor()
   addData = (f"DELETE FROM user_account WHERE id >= 18")
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

login()
table()