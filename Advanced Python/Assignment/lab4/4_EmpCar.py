class Car:

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print("Car Name :", self.name)
        print("Model :", self.model)
        print("Color :", self.color)


class Employee:

    def __init__(self, emp_name, emp_no, car):
        self.emp_name = emp_name
        self.emp_no = emp_no
        self.car = car

    def empinfo(self):
        print("Employee Name :", self.emp_name)
        print("Employee No :", self.emp_no)
        self.car.getinfo()


car1 = Car("BMW", "X5", "Black")

emp = Employee("Vraj", 101, car1)

emp.empinfo()