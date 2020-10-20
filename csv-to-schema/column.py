from enum import Enum


class Type(Enum):
    integer = 0
    float = 1
    string = 3


def is_int(value):
    try:
        int_value = int(value)
    except:
        return False

    return True


def is_float(value):
    try:
        float_value = float(value)
    except:
        return False

    return True


class Column:
    def __init__(self, name):
        self.name = name
        self.values = []

    def add_data(self, value):
        self.values.append(value.strip())

    def calculate_type(self):
        best_type = Type.integer

        if best_type == Type.integer:
            for value in self.values:
                if len(value) > 0 and not is_int(value):
                    best_type = Type.float
                    break

        if best_type == Type.float:
            for value in self.values:
                if len(value) and not is_float(value):
                    best_type = Type.string
                    break

        return best_type

    def as_schema_element(self):
        return '<xs:element name="'+self.name+'" type="xs:'+self.calculate_type().name+'"/>\n'
