#!/usr/bin/env python3
"""7-to_kv.py: Complex types - string and int/float to tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """t takes a string k and an int OR float v as arguments and returns
       a tuple. The first element of the tuple is the string k.
       The second element is the square of the int/float v and should
       be annotated as a float.

    Args:
        k (str): The first element of the tuple
        v (Union[int, float]): The second element is the square

    Returns:
        Tuple[str, float]: returns a tuple
    """
    return (str(k), v * v)
