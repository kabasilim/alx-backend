#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """This function ensures that that if between two queries, certain rows
        are removed from the dataset, the user does not miss items from dataset
        when changing page"""

        result_dict: Dict = {}
        result = []
        dataset_dict = self.indexed_dataset()
        # verify that index is in a valid range.
        assert index <= max(dataset_dict.keys())
        # assert index <= len(self.dataset())
        if index is not None:
            current_index = index
        else:
            current_index = 0
        j = 0
        start = current_index
        size = page_size
        # while j < page_size and start <= max(dataset_dict.keys()):

        while j < size and start <= max(dataset_dict.keys()):
            if dataset_dict.get(start):
                result.append([dataset_dict.get(start)])
            else:
                # if data is not present, we have to maintain the page_size
                # j-= 1
                size += 1
            start += 1
            j += 1
        result_dict['data'] = result
        result_dict['index'] = current_index
        result_dict['next_index'] = start
        result_dict['page_size'] = len(result)

        return result_dict
