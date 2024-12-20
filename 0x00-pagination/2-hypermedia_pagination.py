#!/usr/bin/env python3
"""
Contains method index_range and
class Server
"""


import csv
import math
from typing import List, Tuple, Dict


def index_range(page, page_size) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start
    index and an end index corresponding to the
    range of indexes to return in a list for
    those particular pagination parameters
    """
    start = (page - 1) * page_size
    end = start + page_size

    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """
        Gets pages corresponding to the inputs
        :param page: page to start at
        :param page_size: number of entries to get
        :return: a list of lists containing the data
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        self.dataset()

        if start < end < len(self.__dataset):
            return self.__dataset[start:end]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Performs pagination without taking deletion into consideration
        :param page: starting page
        :param page_size: number of entries to return
        :return: dictionary with data + some relevant information
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': page_size if page < total_pages else 0,
            'page': page,
            'data': data,
            'next_page': page + 1 if page + 1 < total_pages else None,
            'prev_page': page - 1 if 0 < page - 1 < total_pages else None,
            'total_pages': total_pages,
        }
