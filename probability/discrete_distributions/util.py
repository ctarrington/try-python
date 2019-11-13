import math


def n_choose_k(n, k):
    return math.factorial(n)/(math.factorial(k) * math.factorial(n-k))