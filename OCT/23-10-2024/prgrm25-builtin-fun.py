lst = [1,5,342,2345,5743,12342,45,2,8,0]
minimum_value = min(lst)
max_value = max(lst)

length_of_lsit = len(lst)

print(f'Minimum Value of the list is {minimum_value}')
print(f'Maximum Value of the list is {max_value}')
print(f'Length of the list is {length_of_lsit}')
print(f'Sum of list is {sum(lst)}')
lst.sort()
print(f'Sorted List is {lst}')
lst.reverse()
print(lst)
