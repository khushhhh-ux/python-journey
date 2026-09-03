books = {} 
 
def add_books(): 
    while True: 
        book_id = input("Enter Book ID: ") 
 
        if book_id in books: 
            print("Book ID already exists!") 
            continue 
 
        title = input("Enter book title: ") 
        author = input("Enter book author: ") 
 
        books[book_id] = { 
            "title" : title, 
            "author" : author, 
            "available" : True 
        } 
 
        print("Book Added!") 
 
        while True: 
            another = input("Do you want add another book(y/n): ").lower() 
 
            if another in ("y", "n"): 
                break 
        if another == "n": 
            break 
 
def view_books(): 
    print("=====BOOKS=====") 
 
    if not books: 
        print("No Books Added!") 
        return 
 
    for number, (id, data) in enumerate(books.items(), start= 1): 
        print(f"{number}. ID: {id}") 
        print(f"Title: {data['title']}") 
        print(f"Author: {data['author']}") 
 
        if data['available']: 
            status = "Available" 
        else: 
            status = "Borrowed" 
        print(f"Status: {status}") 
        print() 
 
    input("\nPress Enter to return main menu.....") 
 
def search_book(): 
    found = False 
    search = input("Enter book ID or title: ").lower() 
 
    for book_id, data in books.items(): 
 
        if search == book_id.lower() or search in data["title"].lower(): 
            found = True 
 
            print("=====BOOK=====") 
            print(f"ID: {book_id}") 
            print(f"Title: {data['title']}") 
            print(f"Author: {data['author']}") 
 
            if data["available"]: 
                status = "Available" 
            else: 
                status = "Borrowed" 
 
            print(f"Status: {status}") 
            print() 
 
    if not found: 
        print("Book not found!") 
 
    input("\nPress Enter to return main menu.....") 
 
    if not found: 
        print("Book not found") 
 
def borrow_book(): 
    book_id = input("Enter Book ID: ") 
 
    if book_id not in books:  
        print("Book not Found!") 
        return
 
    if book_id in books: 
        book = books[book_id] 
 
        if book['available']: 
            book['available']= False
            print("Book borrowed successfully!")

        else:
            print("Book is already borrowed")

def return_book():
    book_id = input("Enter Book ID: ")

    if book_id not in books:
        print("Book not found!")
        return

    book = books[book_id]

    if book['available']:
        print("Book is already available")

    else:
        book['available'] = True
        print("Book returned successfully!")
        
    input("\nPress Enter to return to main menu...")

def remove_book():
    print("======BOOKS======")
    if not books:
        print("No Books Added!")
        return

    for number, (id, data) in enumerate(books.items(), start= 1): 
        print(f"{number}. ID: {id}") 
        print(f"Title: {data['title']}") 
        print(f"Author: {data['author']}") 
    
        if data['available']: 
            status = "Available" 
        else: 
            status = "Borrowed" 
        print(f"Status: {status}") 
        print() 

    remove = input("Enter the book ID to remove: ")

    if remove in books:
        books.pop(remove)
        print("Book removed!")

    else:
        print("Book not found!")

while True: 
    print("=====LIBRARY MANAGEMENT SYSTEM=====") 
    print("1. Add book") 
    print("2. View book") 
    print("3. Search book") 
    print("4. Borrow book") 
    print("5. Return book") 
    print("6. Remove book") 
    print("7. Exit") 
 
    try: 
        choice = int(input("Enter your choice: ")) 
    except ValueError: 
        print("Invalid choice!") 
        continue 
 
    if choice == 1: 
        add_books() 
 
    elif choice == 2: 
        view_books() 
 
    elif choice == 3: 
        search_book()

    elif choice == 4:
        borrow_book()

    elif choice == 5:
        return_book()

    elif choice == 6:
        remove_book()

    elif choice == 7:
        break

    else:
        print("Wrong choice!")