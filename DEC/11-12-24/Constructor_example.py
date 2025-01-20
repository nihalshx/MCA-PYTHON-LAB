class Employee:
    company = "Red Bull"
    location = "Spielberg"
    def __init__(self,id,name,salary):
        self.id = id 
        self.name = name
        self.salary = salary
    def printDetails(self):
        id = self.id
        name = self.name
        salary = self.salary
        print("Employee Name: ",name)
        print("Employee id: ",id)
        print("Salary: $",salary)
        print()
        
obj = Employee('0','0','0')
print("Company: ",obj.company)
print("Location: ",obj.location)
print()
emp1 = Employee(9281,"Christian Horner",4581000)
emp2 = Employee(1044,"Lewis Hamilton",7200000)
emp3 = Employee(1001,"Max Verstappen",6600000)

emp1.printDetails()
emp2.printDetails()
emp3.printDetails()

        