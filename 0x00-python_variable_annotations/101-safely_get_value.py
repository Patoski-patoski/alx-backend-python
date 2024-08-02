#!/usr/bin/env python3
"""101-safely_get_value.py:More involved type annotations"""

from typing import Mapping, TypeVar,  Union, Sequence, Any
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[None, T]) -> Union[Any, T]:

    """add type annotations to the function

    Hint: look into TypeVar

    def safely_get_value(dct, key, default = None):
        if key in dct:
            return dct[key]
        else:
            return default

        Args:
            dct (Mapping[Any, Any]): dict-like object
            key (Any): key
            default (Union[None, T]): None or generic

        Returns:
            Union[Any, T]: values or None
    """
    if key in dct:
        return dct[key]
    else:
        return default
