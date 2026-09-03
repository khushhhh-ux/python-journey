contacts = {}

while True:
    print("=====CONTACT BOOK=====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please Enter a vaiid choice!")
        continue

    if choice == 1:
        while True:
            contactname = input("Enter the name: ")
            contactnumber = input("Enter the phonenumber: ")
            address = input("Enter the address: ")
            email = input("Enter the email: ")

            contacts[contactname] = {
                "phone": contactnumber,
                "address": address,
                "email": email
            }

            print("Contact Added!")

            while True:
                anothercontact = input("Do you want to add another contact?(y/n): ").lower()

                if anothercontact in ("y", "n"):
                    break

                else: 
                    print("Invalid option")

            if anothercontact == "n":
                break

    if choice == 2:
        print("=====CONTACTS=====")

        for number, (name, data) in enumerate(contacts.items(), start= 1):
            print(f"{number}. name: {name}")
            print(f"   number: {data['phone']}")
            print(f"   address: {data['address']}")
            print(f"   email: {data['email']}")

        print("Press enter to exit!\n")

    if choice == 3:
        searchname = input("Enter name to search: ")

        if searchname in contacts:  
            data = contacts[searchname]
            print(f"name: {searchname}")
            print(f"number: {data['phone']}")
            print(f"address: {data['address']}")
            print(f"email: {data['email']}")

        else:
            print("Contact not found!")

    if choice == 4:
        print("=====CONTACTS=====")
        
        for number, (name, data) in enumerate(contacts.items(), start= 1):
            print(f"{number}. name: {name}")
            print(f"   number: {data['phone']}")
            print(f"   address: {data['address']}")
            print(f"   email: {data['email']}")
        
        removename = input("Enter the name to remove: ")

        if removename in contacts:
            contacts.pop(removename)
            print("Contact removed!")  

        else:
            print("Contact not found!")

    if choice == 5:
        break