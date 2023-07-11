#!/usr/bin/env python3
""" 2-measure_runtime """
import time
import asyncio
acomp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measures the run time """
    start: float = time.perf_counter()
    await asyncio.gather(*(acomp() for _ in range(4)))
    end: float = time.perf_counter() - start
    return end
