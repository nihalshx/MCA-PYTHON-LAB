list=[]
sum=0
size=int(input("Enter size of list :"))
for i in range(size):
    a=(input("Enter the name :"))
    list.append(a)


for j in list:
    count1=j.count('a')
    count2=j.count('A')
    count=count1+count2
    sum+=count


print(f"Total no. of 'a'/'A' in the list: {sum}")