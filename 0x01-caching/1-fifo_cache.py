#!/usr/bin/python3
"""fifo_cache module"""
from collections import deque


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Basic dictionary"""
    def __init__(self):
        """init method"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """Must assign to the dictionary"""
        if (key and item):
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                if self.queue:
                    discarded = self.queue.popleft()
                    del self.cache_data[discarded]
                    print("DISCARD: {}".format(discarded))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """return value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
