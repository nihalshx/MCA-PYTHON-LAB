num=int(input("Enter a number:"))
factorial=1
for fact in range(1,num+1):
    factorial = factorial*fact
print(f"Factorial of {num} : {factorial}")