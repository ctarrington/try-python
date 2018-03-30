
from decimal import Decimal
from fractions import Fraction
import math
import numpy as np


def test_fractions():
    assert Fraction(1, 3) == Fraction('1/3')
    assert Fraction(Decimal('1.1')) == Fraction(11, 10)
    assert Fraction('2/4') == Fraction('1/2')
    assert Fraction('2/4') == 0.50
    assert math.isclose(Fraction('1/3'), 0.3333333333333)


def test_decimals():
    assert Decimal('0.5') == 0.5


def test_raise():
    assert 2**2 == 4
    assert 4**0.5 == 2


def test_convert():
    assert math.ceil(1.01) == 2


def test_distance():
    point_a = np.array([1, 1])
    point_b = np.array([-1, -1])

    # Manhattan or L1 distance
    assert np.linalg.norm((point_a - point_b), ord=1) == 4

    # regular norm aka Euclidian norm aka L2
    assert np.linalg.norm((point_a - point_b)) == 8**0.5


def test_precision():
    ten_tenths = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    assert sum(ten_tenths) != 1
    assert math.isclose(sum(ten_tenths), 1)
    assert math.fsum(ten_tenths) == 1

    hundred_hundreths = [0.01] * 100
    assert math.fsum(hundred_hundreths) == 1

    ten_tenths_np_array = np.full((1, 10), 0.1)
    assert ten_tenths_np_array.sum() == 1

    hundred_hundredths_np_array = np.full((1, 100), 0.01)
    assert hundred_hundredths_np_array.sum() != 1
    assert math.isclose(hundred_hundredths_np_array.sum(), 1)


def test_iteration():
    evens = range(0, 12, 2)
    assert evens[0] == 0
    assert evens[5] == 10

    total = 0
    for num in evens:
        total += num
    assert total == 30

    one_to_ten = range(1, 11)

    # map returns sequence
    tenths = map(lambda x: x / 10, one_to_ten)
    assert next(tenths) == 0.1
    assert next(tenths) == 0.2

    # comprehension returns list
    hundreths = [x / 100 for x in one_to_ten]
    assert hundreths[0] == 0.01
    assert hundreths[1] == 0.02
