#!/usr/bin/env python3
"""wait_n module
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n: waits for a random delay between 0 and max_delay n times

    args:
        n: number of times to wait
        max_delay: maximum delay (default 10)

    returns:
        float: the random delay
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
