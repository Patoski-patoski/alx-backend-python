#!/usr/bin/env python3
"""Tasks"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random: return a asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))


# async def test(max_delay: int) -> float:
#     task = task_wait_random(max_delay)
#    await task
#    print(task.__class__)
#
# asyncio.run(test(5))
