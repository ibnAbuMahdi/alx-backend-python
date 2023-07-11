#!/usr/bin/env python3
""" 1-concurrent_coroutine """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return delays of n async routines """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []
    while tasks:
        done, tasks = await asyncio.wait(tasks,
                                         return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            result = await task
            results.append(result)
    return results
