'''
Remove characters from a string starting from zero up to n and return a new string.
'''    
    
word = input("Enter a word:")

while True:
    
    delete = int(input("How many characters do you want to delete?\n"))

    if delete < len(word):
        deletedWord = word[delete:]
        print(f"New word is: {deletedWord}")
        break
    elif delete == len(word):
        print("You deleted everything man.")
        break
    else:
        print(f"You can delete up to {len(word)} characters, try again.")