#!/usr/bin/env python3
"""Main file"""
import csv
import math
from typing import List, Tuple


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
        """Simple pagination"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start, end = index_range(page, page_size)

        data = self.dataset()[start:end]
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary"""
        titems = len(self.dataset())
        tpages = (titems + page_size - 1)
        start, end = index_range(page, page_size)
        data = self.get_page(page, page_size)
        next_page = page + 1 if page < tpages else None
        prev_page = page - 1 if page > 1 else None
        res = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": tpages
        }

        return res


def index_range(page: int, page_size: int) -> Tuple[int]:
    """return tuple containing start & end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
