#!/usr/bin/env python3
"""This file contains the FIFOCache class"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOCache"""

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
                first = self.cache_keys[0]
                del self.cache_data[first]
                self.cache_keys.pop(0)
                print("DISCARD: {}".format(first))

    def get(self, key):
        """the get method"""
        if key is not None and self.cache_data.get(key):
            return self.cache_data[key]
        else:
            return None
