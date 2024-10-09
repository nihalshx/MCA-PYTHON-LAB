lis=[1,2,3,4,5,6]
print("the given list ",lis)
length=len(lis)-1
temp=lis[0]
lis[0]=lis[length]
lis[length]=temp
print(f"swaped list is {lis}")
