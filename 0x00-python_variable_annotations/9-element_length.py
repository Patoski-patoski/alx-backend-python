#!/usr/bin/env python3
"""9-element_length.py: Let's duck type an iterable object"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below function’s parameters and return values with the
       appropriate types

    def element_length(lst):
    return [(i, len(i)) for i in lst]

    Args:
        lst (Iterable[Sequence]): list to be iterated

    Returns:
        List[Tuple[Sequence, int]]: values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
