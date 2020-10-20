def generate_schema(wrapper, columns):
    schema = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    schema += '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">\n'
    schema += '<xs:element name="'+wrapper+'">\n'
    schema += '<xs:complexType>\n'
    schema += '<xs:sequence>\n'

    for column in columns:
        schema += column.as_schema_element()

    schema += '</xs:sequence>\n'
    schema += '</xs:complexType>\n'
    schema += '</xs:schema>'

    return schema

