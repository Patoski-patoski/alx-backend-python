#!/usr/bin/env python3
"""8-make_multiplier.py: Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a type-annotated function make_multiplier that takes a float multiplier
       as argument and returns a function that multiplies a float by multiplier

    Args:
        multiplier (float):  a float multiplier

    Returns:
        Callable[[float], float]: returns a function that multiplies a float
        by multiplier.
    """
    return lambda num: num * multiplier
