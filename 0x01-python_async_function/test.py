#!/usr/bin/env python3
from typing import List
import asyncio
import random

async def async_rout() -> float:
    """Async routine that returns a random number as a delay"""
    delay = random.uniform(0, 10)
    await asyncio.sleep(delay)
    return delay

async def call_async_rout() -> List[float]:
    """Async routine that calls async_rout() three times"""
    results = []

    tasks = [async_rout() for _ in range(3)]
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
        print(result)

    return results

