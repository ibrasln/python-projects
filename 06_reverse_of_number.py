'''
Print the reverse of the entered number
For example, If the given int is 7536, the output shall be '6357'.
'''

flag = True

while flag:
    number = input("Enter a number:")

    try:
        number = int(number)
    except:
        print("You have to enter a number.")
        continue

    digit_number = 0
    
    while number > 0:
        digit_number = number % 10
        number = number // 10
        print(digit_number, end = '')
        flag = False        
        