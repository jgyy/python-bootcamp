"""
Algebra script
"""
from math import sqrt


class Complex:
    """
    Complex class
    """

    def __init__(self, x, y):
        self.numx = x
        self.numy = y

    def add(self):
        """
        add method
        """
        return Number(
            self.numx.real + self.numy.real, self.numx.imaginary + self.numy.imaginary
        ).show()

    def multi(self):
        """
        multiply method
        """
        return Number(
            self.numx.real * self.numy.real - self.numx.imaginary * self.numy.imaginary,
            self.numy.real * self.numx.imaginary + self.numx.real * self.numy.imaginary,
        ).show()


class Number:
    """
    Number class
    """

    def __init__(self, x, y):
        self.real = x
        self.imaginary = y

    def show(self):
        """
        show method
        """
        print(self.real, self.imaginary)

    def negation(self):
        """
        negation method
        """
        self.real = self.real * -1
        self.imaginary = self.imaginary * -1
        return self

    def inversion(self):
        """
        inversion method
        """
        root = sqrt(self.real * self.real + self.imaginary * self.imaginary)
        self.real = self.real / root
        self.imaginary = -(self.imaginary / root)
        return self


n1 = Number(3, 2)
n2 = Number(1, 1)


n1.negation().show()
n1.inversion().show()

c = Complex(n1, n2)

c.add()

c.multi()
