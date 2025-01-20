from math_operations.basic_operations import arithmetic
from math_operations.geometry import area 

print("Arithmetic Operations")
print("5 + 3",arithmetic.add(5,3))
print("5 - 3", arithmetic.subtract(5,3))
print("5 * 3",arithmetic.multiply(5,3))

print("Area Calculations")
print('Rectangle (length =5, width = 3) = ',area.rectangle_area(5,3))
print('Circle(Radius = 12) = ',area.circle_area(12))
print("Triangle(base = 4, height = 5) = ",area.triangle_area(4,5))