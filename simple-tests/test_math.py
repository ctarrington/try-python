
from decimal import Decimal
from fractions import Fraction
import math
import numpy


def test_fractions():
    assert Fraction(1,3) == Fraction('1/3')
    assert Fraction(Decimal('1.1')) == Fraction(11, 10)
    assert Fraction('2/4') == Fraction('1/2')
    assert Fraction('2/4') == 0.50
    assert math.isclose(Fraction('1/3'), 0.3333333333333) == True 

def test_decimals():
    assert Decimal('0.5') == 0.5

def test_raise():
    assert 2**2 == 4
    assert 4**0.5 == 2

def test_convert():
    assert math.ceil(1.01) == 2

def test_distance():
    a = numpy.array([1,1])
    b = numpy.array([-1, -1])

    # Manhattan or L1 distance
    assert numpy.linalg.norm((a - b), ord=1) == 4

    # regular norm aka Euclidian norm aka L2
    assert numpy.linalg.norm((a-b)) == 8**0.5
