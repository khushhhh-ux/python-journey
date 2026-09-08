import random
import string

while True:
    
    length = int(input("Enter password length: "))

    if length > 0:
        break
    else:
        print("Length must be greater than 0!")

    

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    character = random.choice(characters)
    password += character

print(password)
