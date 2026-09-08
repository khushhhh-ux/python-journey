students = {}
def add_students():
    while True:
        name = input("Enter student name: ")

        try:
            marks = int(input("Enter marks: "))
        except ValueError:
            print("Invalid value!")
            return
        
        students[name] = marks

        print("Student Added!")
        while True: 
            more_students = input("Do you want to add more students(y/n): ").lower()
            
            if more_students in ("y", "n"):
                break
            else:
                print("Invalid option!")

        if more_students == "n":
            break
    
def view_students():
    print("======STUDENTS======")

    for number, (name, marks) in enumerate(students.items(), start=1):
        print(f"{number}. {name}: {marks}")

def calculate_average():
    if len(students)== 0:
        print("No students Added!")
        return
    total = 0

    for marks in students.values():
        total += marks
 
    average = total/len(students) 
    return average
   
while True:
    print("=====STUDENT GRADE MANAGER=====")
    print("1. Add students")
    print("2. View students")
    print("3. Calculate average")
    print("4. Find Top student")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice!")
        continue


    if choice == 1:
        add_students()

    elif choice == 2:
        view_students()

    elif choice == 3:
        print(f"Average: {calculate_average()}")

    elif choice == 4:
        top = max(students.items(), key=lambda item: item[1])
        name, marks = top
        print(f"Top Student: {name}")
        print(f"marks: {marks}")

    elif choice == 5:
        break

    else:
        print("Invalid choice!")