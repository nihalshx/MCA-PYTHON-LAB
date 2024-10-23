input = input("Enter a String ")
print(f'Before Swap {input}')
print(f'After Swapping : {input.replace(input[0], input[len(input) - 1])}')
