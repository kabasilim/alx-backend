#!/usr/bin/env python3
"""This file contains the LFUCache class"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class LFUCache"""

    def __init__(self):
        """Initialization function"""
        super().__init__()
        self.cache_monitor = {}
        self.cache_counter = 0
        self.frequency_monitor = {}

    def put(self, key, item):
        """the put method"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_counter += 1
            self.cache_monitor[key] = self.cache_counter
            if self.frequency_monitor.get(key) is not None:
                self.frequency_monitor[key] =\
                    self.frequency_monitor.get(key) + 1
                new_key = False
            else:
                self.frequency_monitor[key] = 0
                new_key = True

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                temp_dict = self.frequency_monitor.copy()
                if new_key:
                    del temp_dict[key]

                min_frequency = min(temp_dict.values())
                isDistinct = []
                frequencies = {}
                for key, value in temp_dict.items():
                    if value == min_frequency:
                        isDistinct.append(key)
                        frequencies[key] = self.cache_monitor.get(key)
                if len(isDistinct) == 1:
                    lfu = isDistinct[0]
                else:
                    lfu = min(frequencies, key=frequencies.get)
                del self.cache_monitor[lfu]
                del self.cache_data[lfu]
                del self.frequency_monitor[lfu]
                print("DISCARD: {}".format(lfu))

    def get(self, key):
        """the get method"""
        if key is not None and self.cache_data.get(key):
            self.cache_counter += 1
            self.cache_monitor[key] = self.cache_counter
            self.frequency_monitor[key] = self.frequency_monitor.get(key) + 1
            return self.cache_data[key]
        else:
            return None
