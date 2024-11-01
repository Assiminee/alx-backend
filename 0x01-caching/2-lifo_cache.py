#!/usr/bin/env python3
"""
LIFO caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO caching system class
    """
    def __init__(self):
        """Init class method"""
        super().__init__()
        self.order = []

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
            poppedKey = self.order[-1]
            del self.cache_data[poppedKey]
            self.order.remove(poppedKey)

            print("DISCARD: {}".format(poppedKey))

        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)

        self.order.append(key)

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
