#!/usr/bin/env python3
""" 0-basic_async_syntax """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ wait random time and return delay """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
