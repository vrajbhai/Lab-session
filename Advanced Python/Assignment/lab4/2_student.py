class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    
    def __gt__(self,other):
        return self.marks > other.marks
    

st1 =Student("Vraj",100)
st2 =Student("Meet",77)

if st1 > st2:
    print(st1.name)
else:
    print(st2.name)