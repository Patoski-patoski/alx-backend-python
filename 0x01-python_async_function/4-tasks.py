#!/usr/bin/env python3
"""task_wait_n module
"""

import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n: waits for a random delay between 0 and max_delay n times

    Args:
        n: number of times to wait
        max_delay: maximum delay (default 10)

    Returns:
        List[float]: List of random delays
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
