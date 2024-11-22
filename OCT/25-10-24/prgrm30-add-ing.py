strr = input("Enter a string:")
leng = len(strr)
diff = leng-4
if strr[-3:]=="ing":
    strr=strr+"ly"
else:
    strr=strr+"ing"
print(f"{strr}")
