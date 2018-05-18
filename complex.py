#!/usr/bin/env python
import re as reg
from math import sqrt as sq
"""
Alaaddin Alokby
Lab 5: Complex Numbers
Problems: 
Sources: 
https://docs.python.org/2/reference/datamodel.html#emulating-numeric-types
https://docs.python.org/3/tutorial/classes.html
http://mathworld.wolfram.com/ComplexDivision.html
"""

class Complex:
    """A class that performs simple operations on complex numbers"""

    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
        

        # handle imaginary number if entered alone, and as a string
        if type(re) == str and im == 0:
            if 'i' in re:
                im_str = reg.findall(r'\d*i', re)
                im_str = im_str[0][:-1]
                self.re = 0
                self.im = float(im_str)
                
    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __str__(self):
        if self.im < 0:
            return '({} - {}i)'.format(str(self.re),str(-1*self.im))
        return '({} + {}i)'.format(str(self.re), str(self.im))
        

    def __add__(self, other):
        try:
            return Complex(self.re + other.re, self.im + other.im)
        except:
            other = Complex(other)
            return Complex(self.re + other.re, self.im + other.im)

    def __radd__(self, other):
        try:
            return Complex(self.re + other.re, self.im + other.im)
        except:
            other = Complex(other)
            return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        try:
            return Complex(self.re - other.re, self.im - other.im)
        except:
            other = Complex(other)
            return Complex(self.re - other.re, self.im - other.im)

    def __rsub__(self, other):
        try:
            return Complex(self.re - other.re, self.im - other.im)
        except:
            other = Complex(other)
            return Complex(self.re - other.re, self.im - other.im)
    # Complex multiplication - returns float
    def __mul__(self, other):
        try:
            return Complex((self.re * other.re) - (self.im * other.im), (self.re * other.im) + (self.im * other.re))
        except:
            other = Complex(other)
            return Complex((self.re * other.re) - (self.im * other.im), (self.re * other.im) + (self.im * other.re))

    __rmul__ = __mul__
    
    # Using the tilde operator - returns the conjugate
    def __invert__(self):
        return Complex(self.re, -1*self.im)
    # Using the negative operator - returns same magnitude, opposite sign
    def __neg__(self):
        return Complex(-1*self.re, -1*self.im)

    # Complex division - returns integer
    def __floordiv__(self, other):
        try:
            return Complex((self.re*other.re + self.im*other.im)/(other.re**2 + other.im**2),(self.im*other.re - self.re*other.im)/(other.re**2 + other.im**2))
        except AttributeError:
            try:
                other = Complex(other)
                return Complex((self.re*other.re + self.im*other.im)/(other.re**2 + other.im**2),(self.im*other.re - self.re*other.im)/(other.re**2 + other.im**2))
            except ZeroDivisionError:
                return 'ZeroDivisionError: division by zero -- floor'

    def __rfloordiv__(self, other):
        try:
            return Complex((other.re*self.re + other.im*self.im)/(self.re**2 + self.im**2),(other.im*self.re - other.re*self.im)/(self.re**2 + self.im**2))
        except AttributeError:
            try:
                other = Complex(other)
                return Complex((other.re*self.re + other.im*self.im)/(self.re**2 + self.im**2),(other.im*self.re - other.re*self.im)/(self.re**2 + self.im**2))
            except ZeroDivisionError:
                return 'ZeroDivisionError: division by zero -- floorr'

    # Complex division - returns float
    def __truediv__(self, other):
        try:
            return Complex((self.re*other.re + self.im*other.im)/(other.re**2 + other.im**2),(self.im*other.re - self.re*other.im)/(other.re**2 + other.im**2))
        except AttributeError:
            try:
                other = Complex(other)
                return Complex((self.re*other.re + self.im*other.im)/(other.re**2 + other.im**2),(self.im*other.re - self.re*other.im)/(other.re**2 + other.im**2))
            except ZeroDivisionError:
                return 'ZeroDivisionError: division by zero -- true'

    def __rtruediv__(self, other):
        try:
            return Complex((other.re*self.re + other.im*self.im)/(self.re**2 + self.im**2),(other.im*self.re - other.re*self.im)/(self.re**2 + self.im**2))
        except AttributeError:
            try:
                other = Complex(other)
                return Complex((other.re*self.re + other.im*self.im)/(self.re**2 + self.im**2),(other.im*self.re - other.re*self.im)/(self.re**2 + self.im**2))
            except ZeroDivisionError:
                return 'ZeroDivisionError: division by zero -- truer'

# Solve for the square root of a complex number
# Sign Function
# https://en.wikipedia.org/wiki/Complex_number#Square_root
# https://en.wikipedia.org/wiki/Sign_function

#########################################################################################
def sqrt(num):
    try: 
        a = num.re
        b = num.im

        alpha = sq((sq(a**2 + b**2) + a)/2)
        beta = sq((sq(a**2 + b**2) - a) / 2)
        return Complex(alpha, beta)
    except:
        return sq(num)

if __name__ == '__main__':
    c = Complex(17, -5)
    r = Complex(20, 10)
    print(-r)
    print(c)
    print(c/r)
    print((17 - 5j) / (20 + 10j))
    print('#############################')
    print(4j/(17-5j))
    print('4i'/c)
    print(sqrt(Complex(1.23, 3.45)))
    print(sqrt(4))
    print(Complex(5, 3) + Complex(3,5))
    print(Complex(1,2) + '4i' )
    print((Complex(-1, -2) + Complex(-1, -2)) == Complex(-2,-4) )
    print(sq(2+9j))