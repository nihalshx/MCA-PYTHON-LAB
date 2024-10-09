total = 0
mark_list = []

for i in range(5):
    n = int(input(f'Enter mark for Subject {i+1}: '))
    mark_list.append(n)

for mark in mark_list:
    total += mark
percentage = (total / 500) * 100

print(f'Total mark obtained is {total}/500')
print(f'Percentage of mark is {percentage:.2f}%')
