import unittest
from complex import Complex, sqrt
from math import sqrt as sq
import cmath
# class TestCalc(unittest.TestCase):
def test_add():
    truth = 0
    falseth = 0
    for i in range(-10,10):
        for j in range(-10, 10):
            try:
                test_0 = Complex(i,j) + Complex(i,j)
                a = complex(i,j)
                b = complex(i,j)
                c = a+b
                if test_0.re == c.real and test_0.im == c.imag:
                    truth += 1
                else:
                    falseth += 1
            except ZeroDivisionError:
                pass
    if falseth > 0:
        print('Failed addition test {} of 100...'.format(abs(i*j)))
    else: 
        print('Passed {} random addition tests...'.format(abs(i*j)))
    
def test_sub():
    truth = 0
    falseth = 0
    for i in range(-10,10):
        for j in range(-10, 10):
            try:
                test_0 = Complex(i,j) - Complex(i,j)
                a = complex(i,j)
                b = complex(i,j)
                c = a-b
                if test_0.re == c.real and test_0.im == c.imag:
                    truth += 1
                else:
                    falseth += 1
            except ZeroDivisionError:
                pass
    if falseth > 0:
        print('Failed subtraction test {}...'.format(abs(i*j)))
    else: 
        print('Passed {} random subtraction tests...'.format(abs(i*j)))

def test_mult():
    truth = 0
    falseth = 0
    for i in range(-10,10):
        for j in range(-10, 10):
            try:
                test_0 = Complex(i,j) * Complex(i,j)
                a = complex(i,j)
                b = complex(i,j)
                c = a*b
                if test_0.re == c.real and test_0.im == c.imag:
                    truth += 1
                else:
                    falseth += 1
            except ZeroDivisionError:
                pass
    if falseth > 0:
        print('Failed multiplication test {}...'.format(abs(i*j)))
    else: 
        print('Passed {} random multiplication tests...'.format(abs(i*j)))
    
def test_div():
    truth = 0
    falseth = 0
    for i in range(-10,10):
        for j in range(-10, 10):
            try:
                test_0 = Complex(i,j) / Complex(i,j)
                a = complex(i,j)
                b = complex(i,j)
                c = a/b
                if test_0.re == c.real and test_0.im == c.imag:
                    truth += 1
                else:
                    falseth += 1
            except ZeroDivisionError:
                pass
    if falseth > 0:
        print('Failed division test {}...'.format(abs(i*j)))
    else: 
        print('Passed {} random division tests...'.format(abs(i*j)))
    
def test_invert():
    truth = 0
    falseth = 0
    for i in range(-10,10):
        for j in range(-10, 10):
            try:
                test_0 = ~Complex(i,j)
                a = complex(i,j)
                c = complex(i, -j)
                if test_0.re == c.real and test_0.im == c.imag:
                    truth += 1
                else:
                    falseth += 1
            except ZeroDivisionError:
                pass
    if falseth > 0:
        print('Failed inversion test {} of 100...'.format(abs(i*j)))
    else: 
        print('Passed {} random inversion tests...'.format(abs(i*j)))

def test_negation():
    truth = 0
    falseth = 0
    for i in range(-10,10):
        for j in range(-10, 10):
            try:
                test_0 = -Complex(i,j)
                c = complex(-i, -j)
                if test_0.re == c.real and test_0.im == c.imag:
                    truth += 1
                else:
                    falseth += 1
            except ZeroDivisionError:
                pass
    if falseth > 0:
        print('Failed negation test {} of 100...'.format(abs(i*j)))
    else: 
        print('Passed {} random negation tests...'.format(abs(i*j)))

def test_sqrt():
    truth = 0
    falseth = 0
    for i in range(-10,10):
        for j in range(-10, 10):
            try:
                test_0 = sqrt(Complex(i, j))
                c = cmath.sqrt(complex(i, j))
                if test_0.re == c.real and test_0.im == c.imag:
                    truth += 1
                else:
                    falseth += 1
            except ZeroDivisionError:
                pass
    if falseth > 0:
        print('Failed square root test {} of 100...'.format(abs(i*j)))
    else: 
        print('Passed {} random square root tests...'.format(abs(i*j)))

if __name__ == '__main__':
    test_add()
    print('##################')
    test_sub()
    print('##################')
    test_mult()
    print('##################')
    test_div()
    print('##################')
    test_invert()
    print('##################')
    test_negation()
    print('##################')
    test_sqrt()