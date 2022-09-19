'''
You are entering a number between 1 - 100.
Computer is trying to guess your number.
'''

from random import *
import time

live = 8
 
while True:
    num = input("Enter a number between 1 - 100: ")
    
    try:
        num = int(num)
    except:
        print("Input must be a number.")
        continue

    if num >= 1 and num <= 100:
        
        while True:
            guess = randint(1, 101)
           
            print("Computer is guessing your number...")
            time.sleep(1.5)
            print(f"Guess of computer is {guess}.")
           
            if guess == num:
                print("Computer won the game.")
                break
            else:
                print("Computer could not find your number, it is trying again.")
                live -= 1
            print(f"Computer's live is {live}")
            
            if live == 0:
                print("You won the game.")
                break
            
    else:
        print("The number must be between 1 - 100.")



    
    