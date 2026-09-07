class BCA:

    def __init__(self, students):
        self.students = students

    def __add__(self, other):
        return BCA(self.students + other.students)

    def __str__(self):
        return f"Total Students = {self.students}"


fybca = BCA(80)
sybca = BCA(75)
tybca = BCA(70)

total1 = fybca + sybca
print("FY + SY =", total1)

total2 = fybca + sybca + tybca
print("FY + SY + TY =", total2)