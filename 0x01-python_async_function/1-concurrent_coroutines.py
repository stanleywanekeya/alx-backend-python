#!/usr/bin/env python3
"""Task 1"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_random(n: int, max_delay: int) -> List[float]:
    """Executes wait random n times"""
    wait_times = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_Delay), range(n)))
    )
    return sorted(wait_times)
