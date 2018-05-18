#!/usr/bin/env python

from complex import *

def roots(poly):
# A quadratic function is one of the form f(x) = ax2 + bx + c, where a, b, and c are numbers with a not equal to zero.
# http://dl.uncw.edu/digilib/Mathematics/Algebra/mat111hb/PandR/quadratic/quadratic.html
# The argument 'poly' for this function must be in list form.
    
    a, b, c = poly[:]
    
    sq = (b**2 - 4*a*c)

    if sq < 0:
        root_1 = Complex(-b/(2*a), sqrt(-1*sq)/(2*a))      # positive root
        root_2 = Complex(-b/(2*a), -sqrt(-1*sq)/(2*a))     # negative root
        return root_1, root_2

    elif sq > 0:
        root_1 = -b/(2*a) + sqrt(sq)              # positive root
        root_2 = -b/(2*a) - sqrt(sq)              # negative root
    return root_1, root_2

def evaluate(poly, value):
    answer = 0
    for i in range(len(poly)):
        place_holder = 1
        for j in range(len(poly)-1-i):
            place_holder *= value
        answer += poly[i]*place_holder
    return answer

if __name__ == '__main__':
    print(roots([1,-6, 25]))
    print(evaluate([1,2,3], Complex(1,2)))