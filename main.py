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

    global blabel
    blabel = Entry(third)
    blabel.place(x=185,y=40)

    cursor = connection.cursor()
    testQuery = (f"SELECT balance FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        global balance
        balance = item
    connection.commit()
    cursor.close()
    blabel.insert(END, balance)
    
def Deposit(adeposit_amount):
      cursor = connection.cursor()
      deposit = (f"UPDATE user_account SET balance = balance + {adeposit_amount.get()} WHERE name = '{name.get()}' and password = '{password.get()}';")
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
      cursor = connection.cursor()
      withdrawl = (f"UPDATE user_account SET balance = balance - {awithdrawl_amount.get()} WHERE name = '{name.get()}' and password = '{password.get()}';")
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

    lname_label = Label(fourth, text = "Name")
    lname_label.place(x=115,y=75)

    global lname
    lname = Entry(fourth)
    lname.place(x=175,y=75)

    confirm_name_button = Button(fourth, text = "Confirm", command = lambda: Modify_name(lname))
    confirm_name_button.place(x= 310,y= 75)

    cursor = connection.cursor()
    testQuery = (f"SELECT name FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        global alname
        alname = item
    connection.commit()
    lname.insert(END, alname)

    lpassword_label = Label(fourth, text = "Password")
    lpassword_label.place(x=115,y=100)

    global lpassword
    lpassword = Entry(fourth)
    lpassword.place(x= 175, y= 100)

    confirm_password_button = Button(fourth, text = "Confirm", command = lambda: Modify_password(lpassword))
    confirm_password_button.place(x= 310, y= 100)

    testQuery = (f"SELECT password FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        global alpassword
        alpassword = item
    connection.commit()
    lpassword.insert(END, alpassword)    


    lemail_label = Label(fourth, text = "Email")
    lemail_label.place(x= 115, y=125)

    lemail = Entry(fourth)
    lemail.place(x=175, y= 125)
    confirm_email_button = Button(fourth, text = "Confirm", command= lambda: Modify_email(lemail))
    confirm_email_button.place(x= 310, y= 125)

    testQuery = (f"SELECT email FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        global alemail
        alemail = item
    connection.commit()
    lemail.insert(END, alemail)

    cursor.close()
    

    delete_account_button = Button(fourth, text= "Delete Account", command= lambda: delete_account())
    delete_account_button.place(x=115, y=175)
  
def delete_account():
   cursor = connection.cursor()
   addData = (f"DELETE FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
   cursor.execute(addData)

   connection.commit()
   cursor.close()

def Modify_name(lname):
    cursor = connection.cursor()
    name_change = (f"UPDATE user_account SET name = '{lname.get()}' WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(name_change)
    testQuery = (f"SELECT name FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        global alname
        alname = item
    connection.commit()
    connection.commit()
    cursor.close()

def Modify_password(lpassword):
    cursor = connection.cursor()
    password_change = (f"UPDATE user_account SET password = '{lpassword.get()}' WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(password_change)
    connection.commit()
    cursor.close()

def Modify_email(lemail):
    cursor = connection.cursor()
    email_change = (f"UPDATE user_account SET email = '{lemail.get()}' WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(email_change)
    connection.commit()
    cursor.close()
   

def table():
    cursor = connection.cursor()
    testQuery = ("SELECT * FROM user_account")
    cursor.execute(testQuery)

    for item in cursor:
       print(item)

    cursor.close()
login()
table()