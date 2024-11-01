#!/usr/bin/env python3
"""
MRU caching system module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU caching system class
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.usage = []

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
        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            print("DISCARD: {}".format(self.usage[-1]))
            del self.cache_data[self.usage[-1]]
            del self.usage[-1]
        if key in self.usage:
            del self.usage[self.usage.index(key)]
        self.usage.append(key)
        self.cache_data[key] = item

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
