# SET 1
 # 1(a). Count the vowels in a given string
 def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
 # 1(b). Replace all vowels in the string with '#'
 def replace_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels:
            result += "#"
        else:
            result += char
    return result
 # 2. Book and Library Classes
 class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")
    def update_author(self, new_author):
        self.author = new_author
 class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book_name, author, copies):
        self.books.append({"book_name": book_name, "author": author, "copies": copies})
    def lend_book(self, book_name):
        for book in self.books:
            if book["book_name"] == book_name and book["copies"] > 0:
                book["copies"] -= 1
                print(f"Lent out '{book_name}'")
                return
        print(f"'{book_name}' is unavailable")
    def display_books(self):
        for book in self.books:
            print(f"Title: {book['book_name']}, Author: {book['author']}, Copies: {book['copies']}")
 # SET 2
 # 1. Reverse a string and check if it is a palindrome
 def is_palindrome(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s == s
 # 2. Student Class
 class Student:
    def __init__(self):
        self.MCAS1 = []
        self.MCAS3 = []
    def add_student_MCAS1(self, student, position=None):
        if position is None:
            self.MCAS1.append(student)
        else:
            self.MCAS1.insert(position, student)
    def search_student_MCAS1(self, student):
        for s in self.MCAS1:
            if s == student:
                return True
        return False
    def display_all_students(self):
        all_students = []
        for student in self.MCAS1:
            all_students.append(student)
        for student in self.MCAS3:
            all_students.append(student)
        return all_students
 # SET 3
 # Menu-driven program
 class StringProcessor:
    def is_palindrome(self, s):
        reversed_s = ""
        for char in s:
            reversed_s = char + reversed_s
        return reversed_s == s
    def count_vowels(self, s):
        vowels = "aeiouAEIOU"
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        return count
    def reverse_string(self, s):
        reversed_s = ""
        for char in s:
            reversed_s = char + reversed_s
        return reversed_s
 processor = StringProcessor()
 choice = ""
 while choice != "d":
    print("\nMenu:")
    print("a. Check Palindrome")
    print("b. Count Vowels")
    print("c. Reverse String")
    print("d. Exit")
    choice = input("Enter your choice: ")
    if choice == "a":
        string = input("Enter a string: ")
        print("Is palindrome:", processor.is_palindrome(string))
    elif choice == "b":
        string = input("Enter a string: ")
        print("Number of vowels:", processor.count_vowels(string))
    elif choice == "c":
        string = input("Enter a string: ")
        print("Reversed string:", processor.reverse_string(string))
 # 2. Armstrong number
 def read_number():
    return int(input("Enter a number: "))
def is_armstrong(number):
    digits = []
    for d in str(number):
        digits.append(int(d))
    total = 0
    for digit in digits:
        total += digit ** len(digits)
    return total == number
 num = read_number()
 print("Is Armstrong:", is_armstrong(num))
 # SET 4
 # 1. Electricity Bill
 class ElectricityBill:
    def __init__(self, units):
        self.units = units
    def calculate_bill(self):
        if self.units <= 100:
            return self.units * 3.50
        elif self.units <= 200:
            return (100 * 3.50) + (self.units - 100) * 4.50
        else:
            return (100 * 3.50) + (100 * 4.50) + (self.units - 200) * 6.00
 bill = ElectricityBill(250)
 print("Bill amount:", bill.calculate_bill())
 # 2. Lambda Functions for Area
 area_square = lambda side: side * side
 area_rectangle = lambda length, breadth: length * breadth
 area_triangle = lambda base, height: 0.5 * base * height
 print("Area of square:", area_square(5))
 print("Area of rectangle:", area_rectangle(5, 10))
 print("Area of triangle:", area_triangle(10, 6))
 # SET 5
 # 1. Factorial and Fibonacci
 def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
 def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
 print("Factorial of 5:", factorial(5))
 print("First 5 Fibonacci numbers:", fibonacci(5))
 # 2. Four-digit numbers with even digits and perfect squares
 import math
 def find_even_digit_squares(start, end):
    result = []
    for num in range(start, end + 1):
        if int(math.sqrt(num)) ** 2 == num:
            all_even = True
            for digit in str(num):
if int(digit) % 2 != 0:
 all_even = False
 break
 if all_even:
 result.append(num)
 return result
 print("Numbers:", find_even_digit_squares(1000, 9999))