strr = input("Enter a string: ")
countt = set()

for i in strr:
    lower_char = i.lower()
    if lower_char != " " and lower_char not in countt:
        counts = strr.lower().count(lower_char)
        print(f"{lower_char} is {counts}")
        countt.add(lower_char)
