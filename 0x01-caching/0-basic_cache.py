#!/usr/bin/env python3
"""
Contains caching system class BasicCache
"""
from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """
    caching system class
    """
    def put(self, key, item):
        """
        assigns to the dictionary self.cache_data
        (dictionary from the parent class)
        the 'item' value for the key 'key'
        :param key: key to add to the dictionary
        :param item: value to add to the dictionary
        :return: void
        """
        if not key or not item:
            return

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