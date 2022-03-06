'''
Calculate the multiplication and sum of two numbers
Given two integer numbers return their product only if the product is greater than 1000, else return their sum.
''' 

print("If their product is greater than 1000 return product, else return their sum.")

while True:
    number1 = input("Enter the first number:")
    number2 = input("Enter the second number:")

    try:
        number1 = int(number1)
        number2 = int(number2)
    except:
        print("You have to enter a number.")
        continue
    
    product = number1 * number2
    sum = number1 + number2

    if product > 1000:
        print(f"Their product is {product}")
        break
    else:
        print(f"Their product is less than 1000, so their sum is {sum}")
        break
