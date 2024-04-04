#!/usr/bin/env python3
"""This file contains the BasicCache class"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Class BasicCache"""

    def __init__(self):
        """Initialization function"""
        super().__init__()

    def put(self, key, item):
        """the put method"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """the get method"""
        if key is not None and self.cache_data.get(key):
            return self.cache_data[key]
        else:
            return None
