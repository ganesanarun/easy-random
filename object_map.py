object_map = {
    'str': 'random-value',
    'int': 7
}


def value_mapper(type_annotation: type):
    return object_map[type_annotation.__name__]
