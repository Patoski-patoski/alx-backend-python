#!/usr/bin/env python3
"""100-safe_first_element.py: Duck typing - first element of a sequence"""

from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment the following code with the correct duck-typed annotations:
    # The types of the elements of the input are not know
        def safe_first_element(lst):
            if lst:
                return lst[0]
            else:
                return None

        Args:
            lst (Sequence[Any]): Sequence

        Returns:
            Union[Any, None]: None or Any
    """
    if lst:
        return lst[0]
    else:
        return None
