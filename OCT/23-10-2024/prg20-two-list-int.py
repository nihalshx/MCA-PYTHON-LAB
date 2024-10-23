lst1 = []
lst2 = []
same_elements = []
size1 = int(input("Enter size of List 1 "))
size2 = int(input("Enter size of List 2 "))
print('Enter elements of List 1')
for i in range(size1):
    elements1 = int(input(f"Element {i + 1} "))
    lst1.append(elements1)
    
print('Enter elements of List 2')
    
for i in range(size2):
    elements2 = int(input(f"Element {i + 1} "))
    lst2.append(elements2)

# sum_of_1 = sum(lst1)
# sum_of_2 = sum(lst2)


if size1 == size2:
    print(f"Size of List 1 and List 2 is equal {size1}")
else:
    print('Both lists have different Size')

if sum(lst1) == sum(lst2):
    print(f'Sum of List 1 and List 2 is equal {sum(lst1)}')
else:
    print(f'Sum of List 1 = {sum(lst1)}\nSum of List 2 = {sum(lst2)}')
    
for i in lst1:
    if i in lst2:
        print(f'{i} occur in both lists')
