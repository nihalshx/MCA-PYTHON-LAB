n = int(input("How Many numbers do you want? "))
lst = []
for i in range(n):
    if i == 0  or i == 1:
        lst.append(i);
    else:
        number = lst[i - 1] + lst[i - 2]
        lst.append(number)

print(lst)