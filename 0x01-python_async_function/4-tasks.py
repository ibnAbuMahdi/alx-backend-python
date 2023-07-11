#!/usr/bin/env python3
from typing import List
import asyncio
wait = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait(max_delay) for _ in range(n)]
    results = []
    while tasks:
        done, tasks = await asyncio.wait(tasks,
                                         return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            result = await task
            results.append(result)
    return results
