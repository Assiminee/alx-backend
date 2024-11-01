#!/usr/bin/env python3
"""
FIFO caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching system class
    """
    def __init__(self):
        """Init class method"""
        super().__init__()

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

        self.cache_data[key] = item

        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            asciiRep = [ord(dictKey) for dictKey in self.cache_data.keys()]
            poppedKey = chr(min(asciiRep))
            del self.cache_data[poppedKey]

            print("DISCARD: {}".format(poppedKey))

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
