'''
Check if the given number is a palindrome number.
A palindrome number is a number that is same after reverse. For example 131, is the palindrome numbers.
'''
while True:
    origin_number = input("Enter a number: ")
    try:
        origin_number = int(origin_number)
    except:
        print("You have to enter a number.")
        continue
    
    print("Original number is", origin_number)

    number = origin_number
    reverse_num = 0

    while number > 0:
            reminder = number % 10
            reverse_num = (reverse_num * 10) + reminder
            number = number // 10
            
    if origin_number == reverse_num:
        print(origin_number, "is a Palindrome Number.")
        break
    else:
        print(origin_number, "is not a Palindrome Number.")
        break






