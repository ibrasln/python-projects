
letters = 'abcdefghijklmnopqrstuvwxyz'

wordLettersLocation = []

def encrypt(text, word):
    for i in word:
        if i in letters:
            location = letters.find(i)
            wordLettersLocation.append(location)
    
    for i in text:
        if i in letters:
            pass
    
        
        
text = input("Enter a string: ")
word = input("Enter encrypted word: ")

encrypt(text, word)