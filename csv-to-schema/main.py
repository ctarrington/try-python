from column import Column
from generator import generate_schema

file = open('simple.csv', 'r')

headings = file.readline().split(',')
columns = [Column(heading.strip()) for heading in headings]

lines = file.readlines()
for line in lines:
    tokens = line.split(',')
    for index, token in enumerate(tokens):
        columns[index].add_data(token)

schema = generate_schema('sei', columns)
print(schema)
