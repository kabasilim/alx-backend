#!/usr/bin/env python3
"""This file contains the LRUCache class"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Class LRUCache"""

    def __init__(self):
        """Initialization function"""
        super().__init__()
        self.cache_monitor = {}
        self.cache_counter = 0

    def put(self, key, item):
        """the put method"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_counter += 1
            self.cache_monitor[key] = self.cache_counter

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru = min(self.cache_monitor, key=self.cache_monitor.get)
                del self.cache_monitor[lru]
                del self.cache_data[lru]
                print("DISCARD: {}".format(lru))

    def get(self, key):
        """the get method"""
        if key is not None and self.cache_data.get(key):
            self.cache_counter += 1
            self.cache_monitor[key] = self.cache_counter
            return self.cache_data[key]
        else:
            return None
