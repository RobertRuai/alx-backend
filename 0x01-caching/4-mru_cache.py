#!/usr/bin/python3
"""MRU_cache module"""
from collections import OrderedDict


BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Basic dictionary"""
    def __init__(self):
        """init method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Must assign to the dictionary"""
        if (key and item):
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            elif (len(self.cache_data) == BaseCaching.MAX_ITEMS):
                discarded = self.cache_data.popitem(last=True)
                res = dict([discarded])
                for k, v in res.items():
                    print("DISCARD: {}".format(k))
            self.cache_data[key] = item

    def get(self, key):
        """return value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
