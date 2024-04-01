#!/usr/bin/env python3
"""This file contains the Server class"""

import csv
import math
from typing import List, Tuple, Dict, Any, Optional


def index_range(page: int, page_size: int) -> Tuple:
    """This function return a tuple of size two containing a
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination
    parameters"""
    content = 0
    for i in range(1, page):
        content += page_size

    return content, content + page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Server class Initialization"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """This function uses index_range to find the correct indexes to
        paginate the dataset correctly and return the appropriate page of
        the dataset
        """
        assert isinstance(page, int) and page > 0 and\
            isinstance(page_size, int) and page_size > 0
        data = self.dataset()
        page_data = index_range(page, page_size)
        return data[page_data[0]:page_data[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """This function returns a dictionary containing some key-value
        pairs such as page_size, page, data, next_page, previous_page,
        total_pages
        """
        dataset_info: Dict[str, Optional[Any]] = {}
        data = self.get_page(page, page_size)
        data_size = len(data)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        dataset_info['page'] = page
        dataset_info['data'] = data
        dataset_info['page_size'] = data_size
        dataset_info['total_pages'] = total_pages
        if page - 1 > 0:
            dataset_info['prev_page'] = page - 1
        else:
            dataset_info['prev_page'] = None

        if page + 1 <= total_pages:
            dataset_info['next_page'] = page + 1
        else:
            dataset_info['next_page'] = None
        return dataset_info
