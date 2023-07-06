#!/usr/bin/env python3
""" 9-element_length """
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return a list of tuples """
    return [(i, len(i)) for i in lst]
