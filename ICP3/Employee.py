class Employee:  # parent class
    empCount = 0
    tsal = 0
    avgsal = 0

    def __init__(self, name, family, salary, department):  # all parameters
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.empCount += 1
        Employee.tsal += int(salary)

    def average_salary(self):  # here we us this function for caluclating the average value of salary
        print("average salary of %d" % (Employee.tsal / Employee.empCount))

    def explain_interitance(self):
        print("this is output from parent class")

    def print_emp(self):
        print("\nname:", self.name, "family:", self.family, "salary:", self.salary, "department:", self.department)


class Fulltime_Employee(Employee):
    def another_method(self):
        print("this is outpur from child class")


emp1 = Employee("Raji", "Cholleti", "1000", "CS")
emp2 = Employee("Anusha", "Palla", "2000", "EE")
emp3 = Employee("Prakash", "Ravella", "2500", "CS")
emp4 = Employee("Shravya", "Cholelti", "3000", "CS")
emp5 = Fulltime_Employee("Arjun Reddy", "hvcjbcj", "5000", "CS")
print("Total Employee %d" % Employee.empCount)
# this is by function calling
emp1.average_salary()
# displaying output
emp1.print_emp()
emp2.print_emp()
emp3.print_emp()
emp4.print_emp()
# accessing child class
emp5.explain_interitance()
emp5.another_method()
