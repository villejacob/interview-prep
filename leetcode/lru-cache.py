'''
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.

Follow up:
    Could you do both operations in O(1) time complexity?

Example:

    LRUCache cache = new LRUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       # returns 1
    cache.put(3, 3);    # evicts key 2
    cache.get(2);       # returns -1 (not found)
    cache.put(4, 4);    # evicts key 1
    cache.get(1);       # returns -1 (not found)
    cache.get(3);       # returns 3
    cache.get(4);       # returns 4
'''

from collections import OrderedDict 

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.valueOf = OrderedDict()
        

    def get(self, key):
        self.updateKeyUsage(key)
        if key in self.valueOf:
            return self.valueOf[key]
        else:
            return -1


    def updateKeyUsage(self, key):
        if key in self.valueOf:
            value = self.valueOf[key]
            del self.valueOf[key]
            self.valueOf[key] = value
        

    def put(self, key, value):
        if len(self.valueOf) == self.capacity:
            self.valueOf.popitem(last=False)
        self.updateKeyUsage(key)
        self.valueOf[key] = value

    def printOrderedDict(self):
        print self.valueOf
        


# Your LRUCache object will be instantiated and called as such:
capacity = 2
cache = LRUCache(capacity)
cache.put(1, 1);
cache.printOrderedDict()
cache.put(2, 2);
cache.printOrderedDict()
print cache.get(1);       # returns 1
cache.printOrderedDict()
cache.put(3, 3);    # evicts key 2
cache.printOrderedDict()
print cache.get(2);       # returns -1 (not found)
cache.printOrderedDict()
cache.put(4, 4);    # evicts key 1
cache.printOrderedDict()
print cache.get(1);       # returns -1 (not found)
cache.printOrderedDict()
print cache.get(3);       # returns 3
cache.printOrderedDict()
print cache.get(4);       # returns 4
cache.printOrderedDict()
