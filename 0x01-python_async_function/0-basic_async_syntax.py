#!/usr/bin/env python3
"""wait_random module
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random: waits for a random delay between 0 and max_delay

    args:
        max_delay: maximum delay (default 10)

    returns:
        float: the random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
