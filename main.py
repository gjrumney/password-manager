'''
PASSWORD MANAGER

- Allows user to:
    1. Generate passwords
    2. Store passwords with usernames
    3. View password entries
    4. Delete entries
- Option to immediately move generated passwords into storage
'''

import random
import string
import json
import os
from time import sleep

def gen_pass():
    chars = list(string.punctuation + string.ascii_letters + string.digits)
    password = []
    
    
    len_pass = int(input("\nEnter password length: "))
    
    if len_pass:
        for i in range(len_pass):
            randomchar = random.choice(chars)
            password.append(randomchar)
    else:
        return None
        
    password = "".join(password)
    print("\n" + password)
    return password

def gen_store(password, json_path):
    with open(json_path, 'r') as p:
        passwords = json.load(p)
    
    store = input("\nWould you like to store this password? (Y/N) ")
    
    if store.lower() == 'y':
    
        username = input("\nEnter the username: ")
        passwords[username] = password
        with open(json_path, 'w') as p:
            p.write(json.dumps(passwords, indent=2))
            
        print("\nPassword stored!")
        
    elif store.lower() == 'n':
        pass
    
    else:
        print("\nInvalid response.")
        store = input("Would you like to store this password? (Y/N) ")


def store_pass(json_path):
    with open(json_path, 'r') as p:
        passwords = json.load(p)
    
    username = input("Enter the username: ")
    
    if username not in passwords:
        pass
    else:
        print("\nUsername already exists!")
        username = input("Enter a new username: ")
    
    password = input("Enter the password: ")
    
    passwords[username] = password
    with open(json_path, 'w') as p:
        p.write(json.dumps(passwords, indent=2))
    print("\nPassword stored!")
    
def view_pass(json_path):
    with open(json_path, 'r') as p:
        passwords = json.load(p)
    
    for key, value in passwords.items():
        print(f"\nUsername: {key}\nPassword: {value}\n")

def delete_pass(json_path):
    with open(json_path, 'r') as p:
        passwords = json.load(p)
    
    for key, value in passwords.items():
        print(f"\nUsername: {key}\nPassword: {value}\n")   

    deleted = input("\nWhich password do you wish to delete? ")
    try: 
        del passwords[deleted]
        with open(json_path, 'w') as p:
            p.write(json.dumps(passwords, indent=2))
        print("\nPasswords updated!")
        
    except:
        print("\nPassword not found!")
        deleted = input("\nWhich password do you wish to delete? ")

def clear_console():
    os.system('clear')


def main():
    json_path = '/home/george/VSC/Python/passmanage/passwords.json'
    
    while True:
        print("\n1. Generate password" +
            "\n2. Store password" + 
            "\n3. View passwords" +
            "\n4. Delete passwords" +
            "\n5. Exit")
        
        action = int(input("\nSelect a choice (1-4): "))

        if action == 1:
            password = gen_pass()
            gen_store(password, json_path)
            clear_console()
        elif action == 2:
            store_pass(json_path)
            clear_console()
        elif action == 3:
            view_pass(json_path)
            sleep(5)
            clear_console()
        elif action == 4:
            delete_pass(json_path)
            clear_console()
        elif action == 5:
            exit()
        else:
            print("Invalid response.")
            action = int(input("Select a choice (1-4): "))

if __name__ == "__main__":
    clear_console()
    main()