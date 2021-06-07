from typing import TypeVar, get_type_hints

from object_map import value_mapper

T = TypeVar('T')


def next_object(model: T) -> T:
    object_ = model()
    for key, value in get_type_hints(model).items():
        setattr(object_, key, value_mapper(value))
    return object_
