#!/usr/bin/env python3
"""This file contains the LIFOCache class"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Class LIFOCache"""

    def __init__(self):
        """Initialization function"""
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """the put method"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_keys.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last = self.cache_keys[-2]
                self.cache_keys.pop(-2)
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

    def get(self, key):
        """the get method"""
        if key is not None and self.cache_data.get(key):
            return self.cache_data[key]
        else:
            return None
