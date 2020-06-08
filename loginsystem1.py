''' THIS IS A LOGIN SYSTEM PROGRAM.
FIRST, ASK USER FOR A USERNAME/PW
OR ASK THEM TO MAKE AN ACCOUNT.  IF THEY DONT
HAVE AN ACCOUNT, LET THEM MAKE ONE.  ASK FOR
USERNAME, TWO PASSWORDS (CONFIRM PASSWORDS ARE CORRECT)
STORE IN A DATABASE OR TEXT FILE.  ALLOW THE USER TO LOGIN AFTERWARDS.
SAVE INFORMATION AND VALIDATE EVERY
TIME USER LOGINS IN AGAINST TEXT FILE.'''

import time

# this function starts up the login system (menu, etc.)
def StartLoginSystem():
    LoginSuccessful = False  # boolean flag var
    while (LoginSuccessful != True):  # keep running as long as boolean flag is false
        choice = displaymenu() # call the menu to be displayed
        if (choice == 1):  # login to existing account
            LoginSuccessful = loginIn()
        elif (choice == 2):  # creating new account
            createAccount()
        elif (choice == 3):  # Quit the program
            QuitApp()
            break
        else:  # if user types any other number then give error message
            print("Invalid option!")

# this function displays a menu that lets the user pick what they want to do
def displaymenu():
    print("\nWELCOME TO GOOGLE MUSIC SERVICES\n")
    print("1. Login to your account")
    print("2. Create a new account")
    print("3. Quit")
    choice = int(input("\nEnter your choice : "))
    return choice

# This function lets the user login to their account if it exists
def loginIn():
    logSuccess = False
    carlfile = open("GoogleAccounts.txt", "r")  # reads from the text file
    user_name = input("Enter your username : ")
    pass_word = input("Enter your password : ")
    if (carlfile.read() != ""):  # check if the file isnt empty
        userInfoFound = False
        while (userInfoFound != True): # keep running until matching user info is found in the file
            with open("GoogleAccounts.txt") as carlfile: # open the file
                for acc_info in carlfile.readlines(): # go through each line in the file
                    if (acc_info.strip() == (user_name + pass_word)): # check if username and password match the current line
                        userInfoFound = True
                        break
                    else:
                        userInfoFound = False
            if (userInfoFound != True): # if the user info has not been found then ask user to try another username and password
                print("Username or password is invalid!")
                user_name = input("Enter your username : ")
                pass_word = input("Enter your password : ")

        print("Logging in", end="")  # log in after user enters correct account info
        entrymsg = ".........."  # contains the little dots
        for x in entrymsg:  # run a for loop to print out each dot every 0.5 seconds
            print(x, end="")
            time.sleep(0.2)  # controls how long before the next statement prints out
        print("\nLOGIN SUCCESSFUL!")
        logSuccess = True # login was successful so the boolean flag var is true
    else:  # if there is nothing in the file, then the user will get an error message
        print("Your account was not found in our records! You must create a new account!")
    return logSuccess # return the boolean flag var which is true or false

# This function lets the user create an account
def createAccount():
    with open("GoogleAccounts.txt", "a") as carlfile:  # append to the new text file (doesnt clear whats there already)
        email_address = input("Enter an email address : ")
        user_name = input("Enter a username : ")
        pass_word = input("Enter a password : ")
        pass_word2 = input("Confirm the password by typing it again : ")
        while (pass_word2 != pass_word): # check the two passwords match
            print("The second password does not match the first!")
            pass_word2 = input("Confirm the password by typing it again : ")
        carlfile.write(user_name)  # write the user name to the input file and go to next line
        carlfile.write(pass_word + "\n")  # write the password to the input file
        print("Account created successfully!")
        carlfile.close()  # close when done writing to the file
#this function ends the program if the user wants to quit
def QuitApp():
    print("Quitting application", end="")
    endmsg = ".........."  # contains the little dots
    for x in endmsg:  # run a for loop to print out each dot every 0.5 seconds
        print(x, end="")
        time.sleep(0.2)  # controls how long before the next statement prints out

def main():
    with open("GoogleAccounts.txt","w") as carlfile: # open the file to store account info inside of it
        StartLoginSystem() # start the program with this first function
    input("\nPress any key to continue")

main()

