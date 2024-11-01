#!/usr/bin/env python3
"""
LRU caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching system class
    """
    def __init__(self):
        """Init class method"""
        super().__init__()
        self.order = {}

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data
        (dictionary from the parent class)
        the 'item' value for the key 'key'
        :param key: key to add to the dictionary
        :param item: value to add to the dictionary
        :return: void
        """
        if not key or not item:
            return

        cacheSize = len(self.cache_data.keys())

        if cacheSize >= self.MAX_ITEMS and key not in self.cache_data:
            lruKey = min(self.order, key=self.order.get)
            del self.cache_data[lruKey]
            del self.order[lruKey]

            print("DISCARD: {}".format(lruKey))

        self.cache_data[key] = item
        if key in self.order:
            self.order[key] += 1
        else:
            self.order[key] = 1

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        :param key: key to search for
        :return: 'value' from the dictionary if key
        is not null and  exists in the dictionary
        otherwise 'None'
        """
        if key and key in self.cache_data:
            return self.cache_data[key]

        return None
