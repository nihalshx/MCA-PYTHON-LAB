input = input("Enter a string:")
first = input[0]
result = first+input[1:].replace(first.lower(),'$')
print(result)
