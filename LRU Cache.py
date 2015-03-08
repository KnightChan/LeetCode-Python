class LRUCache:
    """ Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item. """

    # @param capacity, an integer
    def __init__(self, capacity):
        self.size = capacity
        self.cache = {}
        self.uselist = []

    # @return an integer
    def get(self, key):
        res = self.cache.get(key)
        if res:
            self.usekey(key)
            return res
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        v = self.cache.get(key)
        if v:
            self.cache[key] = value
            self.usekey(key)
        else:
            if len(self.cache) == self.size:
                okey = self.uselist.pop()
                self.cache.pop(okey)
            self.cache[key] = value
            self.uselist.insert(0, key)

    def usekey(self, key):
        self.uselist.remove(key)
        self.uselist.insert(0, key)

ss = LRUCache(1)
ss.set(2, 1)
ss.get(2)
ss.set(3,2)
ss.get(2)
ss.get(3)