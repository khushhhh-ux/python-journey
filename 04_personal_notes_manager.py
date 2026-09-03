while True:
    print("=====NOTES MANAGER=====")
    print("1. Add notes")
    print("2. View notes")
    print("3. Search notes")
    print("4. Delete notes")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice")
        continue

    if choice == 1:
        note = input("Enter your note: ")

        with open("notes.txt", "a") as f:
            f.write(note + "\n")

        print("Note Added!")

    if choice == 2:
        with open("notes.txt", "r") as f:
            print(f.read())

    if choice == 3:
        searchword = input("Enter a word to search: ")

        with open("notes.txt", "r")as f:
            notes = f.readlines()

        found = False
        for line in notes:
            if searchword in line:
                print(line)
                found = True
                
            if not found:
                print("Word not found")

    if choice == 4:
        print("=====NOTES=====")

        with open("notes.txt", "r") as f:
            notes = f.readlines()
        for number, note in enumerate(notes, start= 1):
            print(f"{number}. {note.strip()}")
        try:
            removenote= int(input("Enter the note to delete: "))
        except ValueError:
            print("Enter a valid value")
            continue

        notes.pop(removenote - 1)

        with open("notes.txt", "w") as f:
            f.writelines(notes)

    if choice == 5: 
        break