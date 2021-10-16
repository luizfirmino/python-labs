#!/usr/bin/env python3

# Assignment 2 - Contact Manager
# Author: Luiz Firmino

# Scope
# Q3. Create a program that a user can use to manage the primary email address and phone number for a contact.
#   a. Use a multi-dimensional list to store the data for the contacts. Provide starting data for two or more contacts.
#   b.  For the view and del commands, display an error message if the user enters an invalid contact number.
#   c. When you exit the program, all changes that you made to the contact list are lost.

CONTACT_LIST = [
        ["Marilyn Monroe", "monroe@gmail.com", "123-435-9889"],
        ["Abraham Lincoln", "AbrahamLincoln@whitehouse.org", "+22 33 4567 4587"]
    ]


def commandList():
    index=1
    for contact in CONTACT_LIST:
        print(index, contact[0])
        index = index + 1
    print()

def commandView():

    while True:
        number = input('Number: ')

        try:
            number = int(number)
            contact = CONTACT_LIST[number-1]
            break
        except ValueError:
            print("Incorrect data format\n")
            continue
        except IndexError:
            print("Number is not available\n")
            continue

    print("Name", contact[0])
    print("E-mail", contact[1])
    print("Phone", contact[2])
    print()


def commandDel():

    while True:
        number = input('Number: ')

        try:
            number = int(number)
            contact = CONTACT_LIST[number-1]
            break
        except ValueError:
            print("Incorrect data format\n")
            continue
        except IndexError:
            print("Number is not available\n")
            continue
    name = CONTACT_LIST[number-1][0]
    CONTACT_LIST.pop(number-1)
        
    print(name, "was deleted")
    print()

def commandAdd():

    name = input('Enter Name: ')
    email = input('Enter E-mail: ')
    phone = input('Enter Phone: ')

    CONTACT_LIST.append([name, email, phone])

    print(name, "was added")
    print()

def getCommand():

    while True:

        command = input('Command: ')

        if command == 'list':
            commandList()
        elif command == 'view':
            commandView()
        elif command == 'add':
            commandAdd()
        elif command == 'del':
            commandDel()
        elif command == 'exit':
            print("Bye!")
            break
        else:
            print("Command invalid")
            continue

def main():

    print("Contact Manager")
    print()

    print("COMMAND MENU")
    print("{:10} {:20}".format("list" , "Display all contacts"))
    print("{:10} {:20}".format("view", "View a contact"))
    print("{:10} {:20}".format("add","Add a contact"))
    print("{:10} {:20}".format("del","Delete a contact"))
    print("{:10} {:20}".format("exit","Exit program"))
    print()

    getCommand()

if __name__ == "__main__":
    main()




