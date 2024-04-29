import mysql.connector
import tkinter
from tkinter import *

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)

window = Tk()


def login():
  window.geometry("400x300")

  label_1 = Label(window, text = "Username")
  label_1.place(x=115,y=75)

  label_2 = Label(window, text = "Password")
  label_2.place(x=115,y=100)

  global name
  name = Entry()
  name.place(x=175, y=75)

  global password
  password = Entry()
  password.place(x=175, y=100)

  btn_1 = Button(window, text = "Login", command= lambda: create_main_page())
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

    confirm = Button(second, text="Confirm", command= lambda: [create_account(abname, abemail, abpassword), abname.delete, abemail.delete, abpassword.delete]) 
    confirm.place(x= 175,y= 150) 
  
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


   
def create_main_page():
    third = Toplevel()
    third.title("Main Page")
    third.geometry("400x300")

    deposit_button = Button(third, text = "Deposit", command= lambda: Deposit(adeposit_amount), height =8, width= 16)
    deposit_button.place(x=85,y=150)

    withdrawl_button = Button(third, text = "Withdrawl", command= lambda: Withdrawl(awithdrawl_amount), height= 8, width= 16)
    withdrawl_button.place(x=210,y=150)

    account_page_button = Button(third, text = "Account", command= lambda:account_window())
    account_page_button.place(x= 340,y=5)

    adeposit_amount = Entry(third)
    adeposit_amount.place(x=85,y=120)

    awithdrawl_amount = Entry(third)
    awithdrawl_amount.place(x=210,y=120)


    cursor = connection.cursor()
    testQuery = (f"SELECT balance FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        global balance
        balance = item
    connection.commit()
    cursor.close()
    global blabel
    blabel = Entry(third)
    blabel.place(x=185,y=40)
    blabel.insert(END, balance)
    
def Deposit(adeposit_amount):
      deposit_amount = adeposit_amount.get()
      cursor = connection.cursor()
      deposit = (f"UPDATE user_account SET balance = balance + {deposit_amount} WHERE name = '{name.get()}' and password = '{password.get()}';")
      cursor.execute(deposit)

      connection.commit()
      cursor.close()

      cursor = connection.cursor()
      testQuery = (f"SELECT balance FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
      cursor.execute(testQuery)
      for item in cursor:
          global balance
          balance = item
      connection.commit()
      cursor.close()
      adeposit_amount.delete(0, 'end')
      blabel.delete(0, 'end')
      blabel.insert(END, balance)


def Withdrawl(awithdrawl_amount):
      withdrawl_amount = awithdrawl_amount.get()
      cursor = connection.cursor()
      withdrawl = (f"UPDATE user_account SET balance = balance - {withdrawl_amount} WHERE name = '{name.get()}' and password = '{password.get()}';")
      cursor.execute(withdrawl)

      connection.commit()
      cursor.close()

      cursor = connection.cursor()
      testQuery = (f"SELECT balance FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
      cursor.execute(testQuery)
      for item in cursor:
          global balance
          balance = item
      connection.commit()
      cursor.close()
      awithdrawl_amount.delete(0, 'end')
      blabel.delete(0, 'end')
      blabel.insert(END, balance)

def account_window():
    fourth = Toplevel()
    fourth.title("Account Page")
    fourth.geometry("400x300")

    lname_label =Label(fourth, text = "Name")
    lname_label.place(x=115,y=75)

    lname = Label(fourth, text = name.get())
    lname.place(x=200,y=75)

    lpassword_label =Label(fourth, text = "Password")
    lpassword_label.place(x=115,y=100)

    lpassword = Label(fourth, text = password.get())
    lpassword.place(x=200, y=100)

    lemail_label = Label(fourth, text = "Email")
    lemail_label.place(x= 115, y=125)

    cursor = connection.cursor()
    testQuery = (f"SELECT email FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        global balance
        email = item
    connection.commit()
    cursor.close()
    lemail = Label(fourth, text = email)
    lemail.place(x=200, y=125)

    delete_account_button = Button(fourth, text= "Delete Account", command= lambda: delete_account())
    delete_account_button.place(x=200, y=150)


def table():
    cursor = connection.cursor()
    testQuery = ("SELECT * FROM user_account")
    cursor.execute(testQuery)

    for item in cursor:
       print(item)

    cursor.close()
    

def delete_account():
   cursor = connection.cursor()
   addData = (f"DELETE FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
   cursor.execute(addData)

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