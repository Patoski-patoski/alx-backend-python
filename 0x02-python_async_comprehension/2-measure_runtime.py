#!/usr/bin/env python3

"""2-measure_runtime.py"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension four times in parallel
       using asyncio.gather.

    Returns:
        float: the total runtime
    """
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.perf_counter() - start_time
