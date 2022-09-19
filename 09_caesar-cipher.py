'''
We will enter a string and our program will encrypt that string.
We can choose step number of Caesar Cipher.
'''


def encrypt(text, step):
      newText = ''
      
      for char in text:
            if char.isupper():
                  newText += chr((ord(char) + step - 65) % 26 + 65)
            elif char.islower:
                  newText += chr((ord(char) + step - 97) % 26 + 97)
      
      return newText

text = input("Enter a string: ")
step = int(input("Enter step number: "))

print(encrypt(text, step))