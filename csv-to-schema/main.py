from column import Column
from generator import generate_schema, generate_xml

file = open('simple.csv', 'r')

headings = file.readline().split(',')
columns = [Column(heading.strip()) for heading in headings]

lines = file.readlines()
for line in lines:
    tokens = line.split(',')
    for index, token in enumerate(tokens):
        columns[index].add_data(token)

wrapper = 'people'
entry = 'person'
schema = generate_schema(wrapper, entry, columns)
schema_file = open('output/'+wrapper+'.xsd', 'w')
schema_file.write(schema)
schema_file.close()

xml = generate_xml(wrapper, entry, columns)
xml_file = open('output/'+wrapper+'.xml', 'w')
xml_file.write(xml)
xml_file.close()