import time
from collections import OrderedDict


class CacheItem(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def get_data(self, key):
        print('Get value %s from cache' % self.value)

    def __repr__(self):
        return 'key:{}, data:{}'.format(self.key, self.value)


class LRUCache(object):

    def __init__(self, size=100, expires=600, region='Montreal'):
        self.expires = expires
        self.size = size
        self.region = region
        self.cache = OrderedDict()
        self.__head = None
        self.__tail = None
   
    def set(self, item):
        timestamp = time.time()
       
        # check if cache is new
        if item.key not in self.cache:
            self.cache[item.key] = (item, timestamp)
        
        # item is not new and is already cached
        else:
            del self.cache[item.key]
            self.__head = list(self.cache.keys())[0]

        if self.__head is None:
            self.__head = item.key

        # check if cache size is bigger than self.size parameter
        if len(self.cache) > self.size:
            del self.cache[self.__head]
            self.__head = list(self.cache.keys())[0]
        
        self.__tail = item.key
    
    def get(self, key):
        if key in self.cache:
            item, _ = self.cache[key]
            del self.cache[key]
            self.cache[key] = (item, time.time())
            self.__tail = key
            item.get_data()
            return item
        raise KeyError('key %s not in cache' % key)

    def remove_expired(self):
        if len(self.cache) == 0:
            return
        first_ts = self.cache[self.__head][1]

        ts = time.time()
        
        # Delete expired item
        expired_items = []
        for k in self.cache.keys():
            if ts - self.cache[k][1] > self.expires:
                expired_items.append(k)
                    
        for k in expired_items:
            del self.cache[k]
    
    def __len__(self):
        return len(self.cache)

    def __contains__(self, key):
        return key in self.cache
