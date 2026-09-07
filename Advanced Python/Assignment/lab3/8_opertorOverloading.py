class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print("Addition =", num1 + num2)


text1 = Number("Dhyey ")
text2 = Number("Patel")

print("Name =", text1 + text2)