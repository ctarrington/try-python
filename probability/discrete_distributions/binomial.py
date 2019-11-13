from discrete_distributions.util import n_choose_k


def probability_of_k_in_n(k, n, p):
    return n_choose_k(n, k) * p**k * (1-p)**(n-k)


def probability_of_k_or_more_in_n(k, n, p):
    ks = range(k, n+1)
    probabilities = [probability_of_k_in_n(k, n, p) for k in ks]
    return sum(probabilities)


p = 0.8
print('n    probability')
for n in range(13, 17):
    combined = probability_of_k_or_more_in_n(10, n, p)
    print(n, '  ', combined)

at_least_10_in_13 = probability_of_k_or_more_in_n(10, 13, p)
print('at_least_10_in_13', at_least_10_in_13)

prob_at_least_16_of_20 = probability_of_k_or_more_in_n(16, 20, 0.5)
print('prob_at_least_16_of_20',prob_at_least_16_of_20)