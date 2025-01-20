class rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w
        
    def Area(self):
        return self.length * self.width
    
    def peri(self):
        return 2*(self.length + self.width)
    
rect1 = rectangle(int(input("Enter len")), int(input("Enter wid")))
rect2 = rectangle(int(input("Enter len")), int(input("Enter wid")))

print(f'Area1: {rect1.Area()}')
print(f'Perimeter1: {rect1.peri()}')
print(f'Area2: {rect2.Area()}')
print(f'Perimeter2: {rect2.peri()}')

if(rect1.Area() ==rect2.Area()):
    print("Areas are same")
elif(rect1.Area() > rect2.Area()):
    print("Rectangle 1 is bigger area")
else:
    print("Areas are not same")
