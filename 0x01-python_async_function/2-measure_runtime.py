#!/usr/bin/env python3
""" 2-measure_runtime """
import time
import asyncio
wait = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the run time """
    start: float = time.perf_counter()
    asyncio.run(wait(n, max_delay))
    end: float = time.perf_counter() - start
    return end / n
