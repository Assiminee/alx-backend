#!/usr/bin/env python3
"""
Contains method index_range and
class Server
"""


import csv
from typing import List, Tuple


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
