names = ['fred', 'wilma', 'barney', 'fred']
people = [{'name': 'fred'}, {'name': 'barney'}, {'name': 'fred'}]

unique_fruits = {'apple', 'banana', 'apple', 'grapefruit'}
uppercase_fruits = {fruit.upper() for fruit in unique_fruits}
fred_list = [person for person in people if person['name'] == 'fred']
fred_name_list = [person['name'].capitalize()
                  for person in people if person['name'] == 'fred']

colors = ['red', 'blue', 'green']
numbers = ['one', 'two', 'three']

number_color_combinations = [number + ' ' +
                             color for number in numbers for color in colors]

number_color_pairs = [pair[0] + ' ' + pair[1]
                      for pair in zip(numbers, colors)]


def test_sets_and_lists():
    assert len(names) == 4          # array keeps duplicate
    assert len(unique_fruits) == 3  # set drops duplicate
    assert 'APPLE' in uppercase_fruits
    assert len(uppercase_fruits) == 3
    assert len(fred_list) == 2
    assert fred_list[0]['name'] == 'fred'
    assert len(fred_name_list) == 2
    assert fred_name_list[0] == 'Fred'
    assert len(number_color_combinations) == 9
    assert number_color_combinations[0] == 'one red'
    assert len(number_color_pairs) == 3
    assert number_color_pairs[0] == 'one red'
    assert number_color_pairs[2] == 'three green'
