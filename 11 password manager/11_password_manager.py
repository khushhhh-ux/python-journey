from cryptography.fernet import Fernet
import os
import json

passwords = {}

def load_or_create_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as file:
            key = file.read()
        return key
    else:
        key = Fernet.generate_key()
        
        with open("key.key", "wb") as file:
            file.write(key)
        return key

def decrypt_password(data):
    decrypted_password = cipher.decrypt(data['password'].encode())
    decrypted_password = decrypted_password.decode()
    print(f"Password : {decrypted_password}")

def add_password():
    while True:
        website = input("Enter website: ")

        if not website:
            print("Website cannot be empty!")
            continue

        if website in passwords:
            print("Website already exists!")
            continue
        
        username = input("Enter username: ")

        if not username:
            print("Username cannot be empty!")
            continue

        password = input("Enter password: ")

        if not password:
            print("Password cannot be empty!")
            continue

        encrypted_password = cipher.encrypt(password.encode())

        passwords[website] = {
            "username": username,
            "password": encrypted_password.decode()
        }

        print("Password Added!")

        while True:
            another = input("Do you want to add another password?(y/n): ").lower()

            if another in ("y", "n"):
                break

        with open("passwords.json", "w") as f:
            json.dump(passwords, f)

        if another == "n":
            break

def load_passwords():
    try:
        with open("passwords.json", "r") as f:
            passwords = json.load(f)
        return passwords

    except FileNotFoundError:
        print("No password file found.")
        return {}

    except json.JSONDecodeError:
        print("Password file is corrupted.")
        return {}

def view_passwords():
    if not passwords:
        print("No passwords saved yet.")
        return

    for number,(website, data) in enumerate(passwords.items(), start=1):
        print(f"{number}. Website: {website}")
        print(f"Username: {data['username']}")

        decrypt_password(data)

def search_password():
    if not passwords:
        print("No passwords saved yet.")
        return

    website = input("Enter website to search: ")

    if not website:
        print("Website cannot be empty!")
        return

    if website in passwords:
        data = passwords[website]

        print(f"Website: {website}")
        print(f"Username: {data['username']}")

        decrypt_password(data)
        
    else:
        print("Website not found!")

key = load_or_create_key()
cipher = Fernet(key)
passwords = load_passwords()

while True:
    print("======PASSWORD MANAGER======")
    print("1. Add password")
    print("2. View passwords")
    print("3. Search password")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print ("Invalid value!")
        continue

    if choice == 1:
        add_password()

    elif choice == 2:
        view_passwords()

    elif choice == 3:
        search_password()

    elif choice == 4:
        break

    else:
        print("Invalid choice!")