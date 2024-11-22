size = int(input("Enter a 4 digit number as size: "))
lst = []

if 1000 <= size <= 9999:
    for num in range(1000, size + 1):
        temp = num
        iseven = True
        
        while temp > 0:
            digit = temp % 10
            if digit % 2 != 0:
                iseven = False
                break
            temp //= 10
            
        if iseven:
            lst.append(num)
        
    for i in lst:
        val = i ** 0.5
        if val == int(val):
            print(f"{i} is a perfect square of {val}")
else:
    print("Enter a 4 digit number!!!!")
