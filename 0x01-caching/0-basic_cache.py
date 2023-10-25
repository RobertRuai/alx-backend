#!/usr/bin/python3
"""basic_cache module"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary"""

    def put(self, key, item):
        """Must assign to the dictionary"""
        if (key and item):
            self.cache_data[key] = item

    def get(self, key):
        """return value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
