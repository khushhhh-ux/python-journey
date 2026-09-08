def quiz():
    question_1 = "Question 1: What is the capital of India?"
    print(question_1)
    answer_1 = input("Answer: ").lower()
    score = 0

    if answer_1 == "delhi":
        print("Correct!")
        score += 1
    else: 
        print("Wrong!")

    question_2 = "Question 2: 2 + 2 = ?"
    print(question_2)
    answer_2 = input("Answer: ")

    if answer_2 == "4":
        print("Correct!")
        score += 1
    else: 
        print("Wrong!")

    question_3 = "Question 3: Which planet is known as the Red Planet?"
    print(question_3)
    answer_3 = input("Answer: ").lower()

    if answer_3 == "mars":
        print("Correct!")
        score += 1
    else: 
        print("Wrong!") 

    print(f"Your final score is {score}/3")

while True:
    quiz()

    again = input("Do you want to play again?(y/n): ")
    if again == "n":
        break









