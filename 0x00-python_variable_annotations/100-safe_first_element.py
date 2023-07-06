#!/usr/bin/env python3
""" 100-safe_first_element """
from typing import Union, Sequence, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ return first element if lst not None """
    if lst:
        return lst[0]
    else:
        return None
