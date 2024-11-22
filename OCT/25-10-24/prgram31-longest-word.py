size = int(input("Enter the size of the list:"))
lst = []
print(f"Enter {size} strings in the list:")
for i in range(size):
    strr = input()
    lst.append(strr)
maxx = max(lst, key=len)
print(f"List items:{lst}\n")
print(f"Longest value in the list:{maxx}")
