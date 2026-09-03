operations = ("+", "-", "/", "*", "%", "**", "//")

def calculations(fnumber, operator, snumber):

    if operator not in operations:
        return "Invalid Operator!"
    
    elif operator == "+":
        return fnumber + snumber

    elif operator == "-":
        return fnumber - snumber

    elif operator == "*":
        return fnumber * snumber

    elif operator == "/":
        if snumber == 0:
            return "Cannot divide by zero!"
        else:
            return fnumber / snumber

    elif operator == "%":
        if snumber == 0:
            return "Cannot divide by zero"
        else:
            return fnumber % snumber

    elif operator == "**":
        return fnumber ** snumber

    elif operator == "//":
        if snumber == 0:
            return "Cannot divide by zero"
        else:
            return fnumber // snumber

while True: 
    print("""
    ====================
         CALCULATOR
    ====================
    1. Calculate
    2. Exit
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            try:
               fnumber = int(input("Enter First Number: "))
               operator = input("Enter Operator(+, -, /, *, %, **, //): ")
               snumber = int(input("Enter Second Number: "))

            except ValueError:
                print("Please enter numbers only!")
                continue

            print(calculations(fnumber, operator, snumber))

            while True:

                n = input("Do you want to calculate again(y/n): ").lower()

                if n == "y":
                    break
                elif n == "n":
                    break
                else:
                    print("Please enter y or n!")
            
            if n == "n":
                break

    elif choice == "2":
        break 
   
    else:
        print("invalid choice!")  
             
