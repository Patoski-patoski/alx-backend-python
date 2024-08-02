#!/usr/bin/env python3
"""102-type_checking.py: Type Checking"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Use mypy to validate the following piece of code and apply any necessary
       changes.

    def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
        zoomed_in: Tuple = [
            item for item in lst
            for i in range(factor)
        ]
        return zoomed_in


    array = [12, 72, 91]

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3.0)

        Args:
            lst (Tuple): first parameter
            factor (int, optional): second parameter. Defaults to 2.

        Returns:
            Tuple: New Tuple
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
