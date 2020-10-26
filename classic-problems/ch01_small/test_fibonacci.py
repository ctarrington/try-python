from unittest import TestCase

from ch01_small.fibonacci import fib


class Test(TestCase):
    def test_fib(self):
        self.assertEquals(fib(10), 55)
