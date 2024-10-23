size = int(input("Enter Size of List "))
colors = []
for i in range(size):
    color = input(f"Enter Color {i + 1} ")
    colors.append(color)
print(colors)
print(f'First Color is {colors[0]}\nLast Color is {colors[size - 1]}')
