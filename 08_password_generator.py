import string
import random
import time

while True:
    
    passwordLength = input("Enter password length: ")

    try:
        passwordLength = int(passwordLength)
    except:
        print("You have to enter a integer.")
        continue

    letters = string.ascii_letters
    digits = string.digits
    specialCharacters = string.punctuation

    characters = letters + digits + specialCharacters
    
    print("Password is generating..")
    password = "".join(random.choice(characters) for x in range(passwordLength))
    time.sleep(1.5)
    print("Password generated.")
    break

print(f"Password is {password}")