#!/usr/bin/env python3
"""Task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random number of seconds"""
    waiting = random.random() * max_delay
    await asyncio.sleep(waiting)
    return waiting
