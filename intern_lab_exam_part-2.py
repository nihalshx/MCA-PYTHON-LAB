# SET 1
 # 1. Program to generate a list of numbers from 1 to N and filter out even numbers.
 def generate_list(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers
 def filter_even_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers
 def cube_of_odd_numbers(numbers):
    cubes = []
    for num in numbers:
        cubes.append(num ** 3)
    return cubes
 n = 10
 numbers = generate_list(n)
 odd_numbers = filter_even_numbers(numbers)
 cubes = cube_of_odd_numbers(odd_numbers)
 print("Original List:", numbers)
 print("Odd Numbers:", odd_numbers)
 print("Cubes of Odd Numbers:", cubes)
 # 2. Package named geometry with modules triangle and circle.
 # geometry/triangle.py
 def triangle_area(base, height):
    return 0.5 * base * height
 def triangle_perimeter(a, b, c):
    return a + b + c
 # geometry/circle.py
 def circle_area(radius):
    return 3.14159 * radius * radius
 def circle_perimeter(radius):
    return 2 * 3.14159 * radius
 # Main Program
 # import geometry.triangle as triangle
 # import geometry.circle as circle
 # SET 2
 # 1. Program to display integers in range 100-200 whose sum of digits is even.
 def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
 def even_digit_sum():
    results = []
    for i in range(100, 201):
        if sum_of_digits(i) % 2 == 0:
            results.append(i)
    return results
 print("Numbers with even sum of digits:", even_digit_sum())
# 2. Employee class.
 class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary
    def update_salary(self, new_salary):
        self.salary = new_salary
    def display_details(self):
        print(f"Name: {self.name}, Designation: {self.designation}, Salary: {self.salary}")
    def calculate_annual_income(self):
        return self.salary * 12
 employees = [
    Employee("Alice", "Manager", 70000),
    Employee("Bob", "Developer", 50000),
    Employee("Charlie", "Designer", 60000)
 ]
 for emp in employees:
    emp.display_details()
 # SET 3
 # Menu-driven program.
 class Operations:
    def occurrence(self, sentence):
        words = sentence.split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count
    def frequency(self, word):
        char_count = {}
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
    def factors(self, number):
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors
 ops = Operations()
 choice = 0
 while choice != 4:
    print("1. Occurrence of word")
    print("2. Character frequency")
    print("3. Factors")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sentence = input("Enter a sentence: ")
        print("Word Occurrence:", ops.occurrence(sentence))
    elif choice == 2:
        word = input("Enter a word: ")
        print("Character Frequency:", ops.frequency(word))
    elif choice == 3:
        number = int(input("Enter a number: "))
        print("Factors:", ops.factors(number))
 # 2. Sort dictionary by descending order of names.
 def sort_students():
    student = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
    sorted_students = sorted(student.items(), key=lambda x: x[0], reverse=True)
    return dict(sorted_students)
 print("Sorted Students:", sort_students())
 # SET 4
 # 1. Rectangle class.
 class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
 rect1 = Rectangle(4, 5)
 rect2 = Rectangle(3, 6)
 if rect1.area() > rect2.area():
    print("Rectangle 1 has a larger area.")
 else:
    print("Rectangle 2 has a larger area.")
 # 2. Find the length of the longest word.
 def longest_word(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length
 words = ["apple", "banana", "cherry", "date"]
 print("Length of the longest word:", longest_word(words))