#!/usr/bin/env python3
"""1-async_comprehension"""

from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension:  collect 10 random numbers using an async
       comprehensing over async_generator

    Returns:
        List[float]: the 10 random numbers from async_generator()
    """
    odd_numbers = [i async for i in async_generator()]
    return odd_numbers
