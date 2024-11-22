# Create a menu driven program to read a list of n numbers from the user 
# and do the following
# 1.find the greatest and lowest number
# 2.sort list in ascending order
# 3.create another list of even numbers
#----------------------------------------------------------------------------#
def find_greatest_and_lowest(numbers):
    if numbers:
        greatest = max(numbers)
        lowest = min(numbers)
        print(f"Greatest number: {greatest}")
        print(f"Lowest number: {lowest}")
    else:
        print("The list is empty.")

def sort_list(numbers):
    sorted_numbers = sorted(numbers)
    print("Sorted list in ascending order:", sorted_numbers)

def create_even_list(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("List of even numbers:", even_numbers)

def main():
    numbers = []
    
    n = int(input("Enter the number of elements: "))

    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    while True:
        print("\nMenu:")
        print("1. Find greatest and lowest")
        print("2. Sort list in ascending order")
        print("3. Create another list of even numbers")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            find_greatest_and_lowest(numbers)
        elif choice == 2:
            sort_list(numbers)
        elif choice == 3:
            create_even_list(numbers)
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
t.append(i)
