#!/usr/bin/env python3
"""
This file contains the index_range function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """This function return a tuple of size two containing a
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination
    parameters"""
    content = 0
    for i in range(1, page):
        content += page_size

    return content, content + page_size
