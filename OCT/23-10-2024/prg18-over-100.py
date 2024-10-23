number_list = []
size = int(input("Enter size "))
for i in range(size):
    item = int(input("Enter Elements "))
    number_list.append(item)
print(number_list)

for i in range(size):
    if(number_list[i] > 100):
        number_list[i] = 'over'

print(number_list)
