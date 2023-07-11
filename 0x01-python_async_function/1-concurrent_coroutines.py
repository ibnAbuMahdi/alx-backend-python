#!/usr/bin/env python3
""" 1-concurrent_coroutines """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[int]:
    """ returns a list of randomly generated delays """
    delays: List[float] = []
    delay: Any = None
    for i in range(n):
        delay = await wait_random(max_delay)
        if (delay is not None):
            delays.append(delay)
    return delays
