object_map = {
    'str': 'random-value'
}


def value_mapper(type_annotation: type):
    return object_map[type_annotation.__name__]
