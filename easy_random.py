import inspect
from typing import Type, List
from typing import TypeVar

T = TypeVar('T')


def next_object(model: T) -> T:
    object_ = model()
    for attr in __getattr__(model):
        setattr(object_, attr, 'random-value')
    return object_


def __getattr__(type_: Type) -> List[str]:
    for i in inspect.getmembers(type_):

        # to remove private and protected
        # functions
        if not i[0].startswith('_'):
            # To remove other methods that
            # does not start with a underscore
            if not inspect.ismethod(i[1]):
                yield i[0]
