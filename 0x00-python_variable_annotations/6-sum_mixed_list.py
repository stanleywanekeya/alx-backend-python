#!/usr/bin/python3
"""Module returning the sum of mixed list and float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> str:
    """Return the sum of mixed int and float"""
    return float(sum(mxd_lst))
