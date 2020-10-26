values = [0,1]


def fill_to(number):
    start = len(values)
    for index in range(start, number+1):
        values.append(values[index-2] + values[index-1])


def fib(number):
    if len(values) > number:
        return values[number]

    fill_to(number)
    return values[number]
