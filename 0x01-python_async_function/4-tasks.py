#!/usr/bin/env python3
"""measure_runtime module
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """measure_time: measure the runtime of wait_n

    args:
        n: number of times to wait
        max_delay: maximum delay (default 10)

    returns:
        float: the runtime
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
