'''
Computer is returning a random number between 1 - 100. 
You have to find this number.
'''

from random import *
 
num = randint(1, 101)
live = 8
print("Welcome the Guess Number Game. You have only 8 lives.")
while True:
    guess = input("Enter your guess:")
    
    try:
        guess = int(guess)
    except:
        print("You have to enter a number.")
        continue
        
    if guess >= 1 and guess <= 100:
        
        if guess == num:
            print("Congratulations, you guessed the number correctly.")
            break
        
        elif guess > num:
            print("Your guess is bigger than number.")
            live -= 1
        
        elif guess < num:
            print("Your guess is lower than number.")
            live -= 1
        print(f"{live} lives left.")
    else:
        print("Your guess must be between 1 - 100.")

    if live == 0:
        print(f"Sorry, you could not find the number.\nThe number was {num}.")
        break