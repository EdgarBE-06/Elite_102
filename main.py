import mysql.connector
import tkinter
from tkinter import *

#creates the connection to the mysql database
connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_account',
    password = 'password'
)

#Creates a window
window = Tk()


def login():
  #Decides the size of the window
  window.geometry("400x300")

  #Writes and places text in the window
  label_1 = Label(window, text = "Username")
  label_1.place(x=115,y=75)

  label_2 = Label(window, text = "Password")
  label_2.place(x=115,y=100)

  #Places input boxes into the window
  global name
  name = Entry()
  name.place(x=175, y=75)

  global password
  password = Entry()
  password.place(x=175, y=100)

  #Creates and places buttons in the window
  #Login Button that opens the main page
  btn_1 = Button(window, text = "Login", command= lambda: create_main_page())
  btn_1.place(x=175,y=125)

  #Sign up button that opens the sign up page
  btn_2 = Button(window, text = "Sign up", command= lambda: create_account_window())
  btn_2.place(x= 225,y= 125)

  #Allows the window to run and put things in it
  window.mainloop()

#Function that creates a new window for creating an account
def create_account_window():
    #Opens a new window
    second = Toplevel()
    #Names the new window
    second.title("Sign up page")
    #Sizes the new window
    second.geometry("400x300")

    #Writes text in the new window
    clabel_1 = Label(second, text ="Username")
    clabel_1.place(x=100,y=75)
    #Creates a place for inputs in the new window to take in username
    abname = Entry(second)
    abname.place(x=175,y=75)

    #Writes text in the new window
    clabel_2 = Label(second, text ="Email")
    clabel_2.place(x=100,y = 100)
    #Creates a place for inputs in the new window to take in email
    abemail = Entry(second)
    abemail.place(x=175,y=100)
    
    #Writes text in the new window
    clabel_3 = Label(second, text="Password")
    clabel_3.place(x=100,y = 125)
    #Creates a place for inputs in the new window to take in password
    abpassword = Entry(second)
    abpassword.place(x=175,y=125)

    #Creates a button that runs the create account function 
    confirm = Button(second, text="Confirm", command= lambda: [create_account(abname, abemail, abpassword), abname.delete, abemail.delete, abpassword.delete]) 
    confirm.place(x= 175,y= 150) 
  
#Function to create an account and add it into the database
def create_account(abname, abemail, abpassword):
   #Sets the default balance of the created account to 0
   abalance = 0
   #Uses the connection to mysql
   cursor = connection.cursor()
   #Take in the data from the user Entries and puts it into the mysql database
   addData = (f"INSERT INTO user_account (name, email, password, balance)VALUES ('{abname.get()}','{abemail.get()}','{abpassword.get()}', {abalance})")
   #runs add data and closes the connection
   cursor.execute(addData)

   connection.commit()
   cursor.close()

#Function to create the main page
def create_main_page():
    #Creates a new window, titels it, and sizes it 
    third = Toplevel()
    third.title("Main Page")
    third.geometry("400x300")

    #Creates a button to run the deposit function taking in a number from the user
    deposit_button = Button(third, text = "Deposit", command= lambda: Deposit(adeposit_amount), height =8, width= 16)
    deposit_button.place(x=85,y=150)

    #Creates a button to run the withdrawl function taking in a number from the user
    withdrawl_button = Button(third, text = "Withdrawl", command= lambda: Withdrawl(awithdrawl_amount), height= 8, width= 16)
    withdrawl_button.place(x=210,y=150)

    #Creates a button to run the account window function
    account_page_button = Button(third, text = "Account", command= lambda:account_window())
    account_page_button.place(x= 340,y=5)

    #Creates places for Deposit and Withdrawl numbers to go into the functions
    adeposit_amount = Entry(third)
    adeposit_amount.place(x=85,y=120)

    awithdrawl_amount = Entry(third)
    awithdrawl_amount.place(x=210,y=120)

    #Creates a way to display balance using an entry, Entry is used to make live changes
    global blabel
    blabel = Entry(third)
    blabel.place(x=185,y=40)

    #Uses mysql connection
    cursor = connection.cursor()
    #Selects the balance from the database in the row where the name and password matches the user inputs from the login
    testQuery = (f"SELECT balance FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        #Take the selected balance and turn it into a global variable to be changed in the deposit and withdrawl functions
        global balance
        balance = item
    connection.commit()
    cursor.close()
    #Places the balance into the Entry
    blabel.insert(END, balance)

#Creates a function to Deposit money into the account by adding to the balance    
def Deposit(adeposit_amount):
      cursor = connection.cursor()
      #Takes in the deposit input and adds it to the balance in the row where name and password matches the login
      deposit = (f"UPDATE user_account SET balance = balance + {adeposit_amount.get()} WHERE name = '{name.get()}' and password = '{password.get()}';")
      cursor.execute(deposit)

      connection.commit()
      cursor.close()

      cursor = connection.cursor()
      #Selects the new balance from the database 
      testQuery = (f"SELECT balance FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
      cursor.execute(testQuery)
      for item in cursor:
          #Changes the old balance variable to the new balance
          global balance
          balance = item
      connection.commit()
      cursor.close()
      #Deletes the text in the balance and deposit entries and puts the new balance into the balance entry
      adeposit_amount.delete(0, 'end')
      blabel.delete(0, 'end')
      blabel.insert(END, balance)

#Creates a function to Withdrawl money from the account by subtracting from the balance
def Withdrawl(awithdrawl_amount):
      cursor = connection.cursor()
      #Takes in the withdrawl input and subtracts it from the balance in the row where name and password matches the login
      withdrawl = (f"UPDATE user_account SET balance = balance - {awithdrawl_amount.get()} WHERE name = '{name.get()}' and password = '{password.get()}';")
      cursor.execute(withdrawl)

      connection.commit()
      cursor.close()

      cursor = connection.cursor()
      #Selects the new balance from the database
      testQuery = (f"SELECT balance FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
      cursor.execute(testQuery)
      for item in cursor:
          global balance
          balance = item
      connection.commit()
      cursor.close()
      #Deletes the text in the balance and withdrawl entries and puts the new balance into the balance entry
      awithdrawl_amount.delete(0, 'end')
      blabel.delete(0, 'end')
      blabel.insert(END, balance)

#Function to create the window to display and change account information as well as delete the account
def account_window():
    #Creates, titles, and sizes the window
    fourth = Toplevel()
    fourth.title("Account Page")
    fourth.geometry("400x300")

    #Displays text to show Name
    lname_label = Label(fourth, text = "Name")
    lname_label.place(x=115,y=75)

    #Creates a place to display the user's name and where to change it
    global lname
    lname = Entry(fourth)
    lname.place(x=175,y=75)

    #Button to run the Modify_name button using the name Entry
    confirm_name_button = Button(fourth, text = "Confirm", command = lambda: Modify_name(lname))
    confirm_name_button.place(x= 310,y= 75)

    #Selects the name from the database that matches the login and puts it into the Entry
    cursor = connection.cursor()
    testQuery = (f"SELECT name FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        global alname
        alname = item
    connection.commit()
    lname.insert(END, alname)

    #Display text to show Password
    lpassword_label = Label(fourth, text = "Password")
    lpassword_label.place(x=115,y=100)

    #Creates a place to display the user's password and where to change it 
    global lpassword
    lpassword = Entry(fourth)
    lpassword.place(x= 175, y= 100)

    #Button to run the Modify_password button using the password Entry
    confirm_password_button = Button(fourth, text = "Confirm", command = lambda: Modify_password(lpassword))
    confirm_password_button.place(x= 310, y= 100)

    #Selects the password from the database that matches the login and puts it into the Entry
    testQuery = (f"SELECT password FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        global alpassword
        alpassword = item
    connection.commit()
    lpassword.insert(END, alpassword)    


    #Creates text to show Email
    lemail_label = Label(fourth, text = "Email")
    lemail_label.place(x= 115, y=125)

    #Creates a place to displays the users email and where to change it
    lemail = Entry(fourth)
    lemail.place(x=175, y= 125)
    #Button to run the Modify Email function using the email entry
    confirm_email_button = Button(fourth, text = "Confirm", command= lambda: Modify_email(lemail))
    confirm_email_button.place(x= 310, y= 125)

    #Selects the email from the database that matches the login and puts it into the Entry
    testQuery = (f"SELECT email FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(testQuery)
    for item in cursor:
        global alemail
        alemail = item
    connection.commit()
    lemail.insert(END, alemail)

    cursor.close()
    

    #Creates a button to run the delete account function
    delete_account_button = Button(fourth, text= "Delete Account", command= lambda: delete_account())
    delete_account_button.place(x=115, y=175)
  

#Deletes the row from the database that matches the login 
def delete_account():
   cursor = connection.cursor()
   addData = (f"DELETE FROM user_account WHERE name = '{name.get()}' and password = '{password.get()}'")
   cursor.execute(addData)

   connection.commit()
   cursor.close()

#Function that changes the name in the database where name and password matches the login
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

#Function that changes the password in the database where name and password matches the login
def Modify_password(lpassword):
    cursor = connection.cursor()
    password_change = (f"UPDATE user_account SET password = '{lpassword.get()}' WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(password_change)
    connection.commit()
    cursor.close()

#Function that changes the email in the database where name and password matches the login
def Modify_email(lemail):
    cursor = connection.cursor()
    email_change = (f"UPDATE user_account SET email = '{lemail.get()}' WHERE name = '{name.get()}' and password = '{password.get()}'")
    cursor.execute(email_change)
    connection.commit()
    cursor.close()
   
#Function to display the mysql database in the terminal(My primary testing tool which
#allowed me to quickly see if any changes had been made to the database)
def table():
    #Selects everything from the database and prints all of it
    cursor = connection.cursor()
    testQuery = ("SELECT * FROM user_account")
    cursor.execute(testQuery)

    for item in cursor:
       print(item)

    cursor.close()

login()
table()