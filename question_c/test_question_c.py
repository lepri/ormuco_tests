import uuid
import time
import unittest

from cache import LRUCache, CacheItem


def generate_content(n=10):
    content = []
    for i in range(1, n+1):
        username = 'item%s' % i
        visited_page = uuid.uuid4().hex
        item = CacheItem(username, visited_page)
        content.append(item)
    return content


class TestLRUCache(unittest.TestCase):
    
    def test_expiration(self):
        cache = LRUCache(size=1000, expires=3 , region='Montreal')
        content = generate_content(n=10)
        for item in content:
            cache.set(item)

        self.assertEqual(len(cache), 10)
        time.sleep(3)
        cache.remove_expired()
        self.assertTrue(len(cache) == 0)

        # remove expired items
        item1 = content[0]
        cache.set(item1)
        time.sleep(3)
        for item in content[9:]:
            cache.set(item)
        cache.remove_expired()
        self.assertEqual(len(cache), 1)
    
    def test_size(self):
        cache = LRUCache(size=5, expires=1000 , region='Montreal')
        users = generate_content(n=10)
        for user in users:
            cache.set(user)

        # test max capacity of cache
        self.assertEqual(len(cache), 5)

        # users == 10 but we dont have 10 items in cache
        self.assertNotEqual(len(cache), 10)


if __name__ == '__main__':
    unittest.main()
