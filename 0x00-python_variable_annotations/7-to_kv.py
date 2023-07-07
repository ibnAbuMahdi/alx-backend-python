#!/usr/bin/env python3
""" 7-to_kv """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return a tuple """
    tup: Tuple[str, float]
    tup = (k, float(v)**2)
    return tup
