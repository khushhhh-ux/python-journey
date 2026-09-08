import json

def add_entry():
    while True:
        try:
            with open("journal.json", "r") as f:
                entries= json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No entries exists!")
            entries = []
        
        date = input("Enter date: ")
        text  = input("Write your entry: ")

        journal = {
            "date": date,
            "text":text
        }

        entries.append(journal)

        print(entries)

        with open("journal.json", "w") as f:
            json.dump(entries, f)

        while True:
            another = input("Do you want add another entry(y/n): ").lower()

            if another in ("y" ,"n"):
                break
        if another == "n":
            break

def view_entries():
    try: 
        with open("journal.json", "r")as f:
            entries = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No entry exist!")
        return

    for number, entry in enumerate(entries, start=1):
        print(f"{number}. {entry['date']}")
        print(f"{entry['text']}")
                  
def search_entries():
    search = input("Enter a word to search: ").lower()

    try:
        with open("journal.json")as f:
            entries = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        print("No entries exists!")
        return

    found = False

    for entry in entries:
        if search in entry["text"].lower():
            print(entry)
            found = True

    if not found:
        print("Entry not found!")

def delete_entry():
    try:
        with open("journal.json", "r") as f:
            entries = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No entry exist!")
        return
    
    for number, entry in enumerate(entries, start=1):
        print(f"{number}. {entry['date']}")
        print(f"{entry['text']}")    
    try:
        delete = int(input("Enter entry number to delete: "))
    except ValueError:
        print("Choose correct value!")
        return  

    if delete < 1 or delete > len(entries):
        print("Invalid entry number!")
        return

    entries.pop(delete - 1)    

    with open ("journal.json", "w")as f:
        json.dump(entries, f)

while True:
    print("===== DAILY JOURNAL =====")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Search Entries")
    print("4. Delete Entry")
    print("5. Exit")

    try:
        choice= int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice!")
        continue

    if choice== 1:
        add_entry()

    elif choice== 2:
        view_entries()

    elif choice == 3:
        search_entries()
    
    elif choice == 4:
        delete_entry()

    elif choice == 5:
        break
