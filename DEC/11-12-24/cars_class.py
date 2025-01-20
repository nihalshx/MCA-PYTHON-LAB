class Cars:
    company = ' '
    price = ' '
    color = ''
    def printCars(self):
        company = self.company
        price = self.price
        color = self.color
        print(f'This Car  is a {color} colored {company} which is priced at {price}')
    
car1 = Cars()
car2 = Cars()
car3 = Cars()

car1.company = 'Skoda'
car1.price = '$46000'
car1.color = 'Black'

car2.company = 'Hyundai'
car2.price = '$69000'
car2.color = 'Orange'

car3.company = 'Cadillac'
car3.price = '$12007'
car3.color = 'Yellow'

print("Car 1 Details")
car1.printCars()
print()
print("Car 2 Details")
car2.printCars()
print()
print("Car 3 Details")
car3.printCars()
