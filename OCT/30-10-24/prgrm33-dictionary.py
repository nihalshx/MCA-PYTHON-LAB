#program to print a dictionary where the keys
#are numbers between 1 and 15
#and the values are the squares of the keys.

# a = {}
# for i in range(1,16):
#     a[i] = i * i
# print(a)



size = 16
keys = []
values = []
dictionary = {}
for i in range(1,size):
    keys.append(i)
    
for i in range(1,size):
    values.append(i * i)

for i in range(size-1):
    dictionary[keys[i]] = values[i] 


print(dictionary)
