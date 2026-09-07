class Employee:

    def __init__(self, name, salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

    def __mul__(self, working_days):
        total_salary = self.salary_per_day * working_days.days
        return total_salary


class WorkingDays:

    def __init__(self, days):
        self.days = days


employee = Employee("Vraj", 1000)

month = WorkingDays(26)

salary = employee * month

print("Employee Name :", employee.name)
print("Monthly Salary :", salary)