#!/usr/bin/env python3
""" 0-async_generator """
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ yields a random number between 1 and 10 10x asynchronously"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
