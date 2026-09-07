class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


num1 = Complex(1, 2)
num2 = Complex(2, 3)

num3 = num1 + num2

print(num3)