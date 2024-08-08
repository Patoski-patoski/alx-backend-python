#!/usr/bin/env python3

"""0-async_generator.py"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float]:
    """async_generator:a coroutine called async_generator that takes no
       arguments.

    Yields:
        _type_: a random number between 0 and 10
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
