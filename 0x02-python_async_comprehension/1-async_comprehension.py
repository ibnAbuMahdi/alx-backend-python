#!/usr/bin/env python3
""" 1-async_comprehension """
from typing import List
agen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ return comprehension list of async generated numbers """
    return [i async for i in agen()]
