expensedict = {}

while True:
    print("======EXPENSE TRACKER=====")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Remove Expenses")
    print("4. Exit")

    try:
        choice = int(input("Enter a choice: "))
    except ValueError:
        print("Enter the correct value!")
        continue

    if choice == 1:
        while True:
            try:
                expensename = input("Enter expense name: ")
                expenseamount = int(input("Enter amount: "))
                category = input("Enter category: ")
                
            except ValueError:
                print("Enter the value correctly!")
                continue
            
            expensedict[expensename] = expenseamount, category
            
            print("Expense Added!")

            while True:
                active = input("Add another expense?(y/n): ").lower()
                
                if active == "n":
                    break

                elif active == "y":
                    break
                    
                else:
                    print("Invalid option")

            if active == "n":
                break

    if choice == 2:
        total = 0
        print("======EXPENSES======")

        for name, data in expensedict.items():
            amount, category = data

            total += amount
            print(f"{name}: {amount} | Category: {category}")

        print(f"Total amount: {total}")
        print("Press Enter to Exit\n")

    if choice == 3:
        print("======EXPENSES======")
        for number, (name, data) in enumerate (expensedict.items(), start=1):
            amount, category = data

            print(f"{number}. {name}: {amount} | Category: {category}")
        try:
            remove = int(input("Enter expense number to remove: "))

        except ValueError:
            print("Enter the correct value!")
            continue

        names = list(expensedict.keys())
        if 1<= remove <= len(names):
            expensedict.pop(names[remove - 1])
            print("Expense Removed!")
        else:
            print("Invalid Expense number!")
            
    if choice == 4:
        break

            
