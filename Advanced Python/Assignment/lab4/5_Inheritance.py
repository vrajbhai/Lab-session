class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatanddrink(self):
        print("Eat Spicy FOod and Drink Chill Chhas")


class Employee(Person):

    def __init__(self, name, age, emp_no, emp_salary):
        super().__init__(name, age)
        self.emp_no = emp_no
        self.emp_salary = emp_salary

    def empinfo(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Employee No :", self.emp_no)
        print("Salary :", self.emp_salary)


emp = Employee("Vraj", 20, 101, 50000)

emp.eatanddrink()
emp.empinfo()