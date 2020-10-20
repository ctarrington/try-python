def generate_schema(wrapper, entry, columns):
    schema = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    schema += '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">\n'

    schema += '<xs:element name="'+wrapper+'" type="'+wrapper+'Type" />\n\n'

    schema += '<xs:complexType name="'+wrapper+'Type">\n'
    schema += '<xs:sequence>\n'
    schema += '<xs:element name="'+entry+'" type="'+entry+'Type" minOccurs="0" maxOccurs="unbounded"/>\n'
    schema += '</xs:sequence>\n'
    schema += '</xs:complexType>\n\n'

    schema += '<xs:complexType name="'+entry+'Type">\n'
    schema += '<xs:sequence>\n'

    for column in columns:
        schema += column.as_schema_element()

    schema += '</xs:sequence>\n'
    schema += '</xs:complexType>\n'
    schema += '</xs:schema>'

    return schema


def generate_row(entry, columns, row_ctr):
    row = '<' +entry+'>\n'
    for column in columns:
        value = column.values[row_ctr]
        if len(value) > 0:
            row += '<' +column.name+'>'
            row += value
            row += '</' + column.name + '>\n'
    row += '</'+entry+'>\n'
    return row


def generate_xml(wrapper, entry, columns):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<'+wrapper+' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
    xml += 'xsi:noNamespaceSchemaLocation="'+wrapper+'.xsd">\n'

    row_count = len(columns[0].values)
    for row_ctr in range(row_count):
        xml += generate_row(entry, columns, row_ctr)

    xml += '</'+wrapper+'>\n'

    return xml

