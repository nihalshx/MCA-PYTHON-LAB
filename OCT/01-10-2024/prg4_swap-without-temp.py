number1 = int(input("Enter First number"))
number2 = int(input("Enter second number"))
print(f'Before Swapping No.1 = {number1}, No.2 = {number2}')

number1 = number1 + number2 # n1 = 10, n2 = 20, now n1 = 30
number2 = number1 - number2 # n2 = 30 - 20 = 10
number1 = number1 - number2 # n1 = 30 - 10 = 20

print(f'After Swapping No.1 = {number1}, No.2 = {number2}')
