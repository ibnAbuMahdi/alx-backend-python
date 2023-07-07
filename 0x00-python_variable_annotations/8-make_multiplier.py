#!/usr/bin/env python3
""" 8-make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a Callable type """
    def f(inp: float) -> float:
        return multiplier * inp
    clb: Callable[[float], float] = f
    return clb
