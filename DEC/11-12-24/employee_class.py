class employee:
    basic_salary = 0
    ta = 0
    da = 0
    def salary(self):
        result  = self.basic_salary + self.ta + self.da
        print("Salary is ",result)
        
emp1 = employee()
emp2 = employee()

emp1.basic_salary = 98000
emp1.ta = 5400
emp1.da = 1200

emp2.basic_salary = 78000
emp2.ta = 5100
emp2.da = 1900

emp1.salary()
emp2.salary()


