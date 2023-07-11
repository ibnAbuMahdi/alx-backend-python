#!/usr/bin/env python3
""" 3-tasks """
import asyncio
wait = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ returns task """
    return asyncio.create_task(wait(max_delay))
