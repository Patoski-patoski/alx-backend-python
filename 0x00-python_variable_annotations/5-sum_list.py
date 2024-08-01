#!/usr/bin/env python3
"""5-sum_list.py: takes a list input_list of floats as argument and returns
   their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list input_list of floats as argument and returns their sum as a
       float.

    Args:
        input_list (List[float]): annotated list

    Returns:
        float: sum of the floats in the list
    """
    return sum(input_list)
