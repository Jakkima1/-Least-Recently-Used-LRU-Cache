import unittest2

from LRU import LRUCache


class MyTestCase(unittest2.TestCase):
    def test_size(self):
        lru = LRUCache(1)
        assert lru.capacity == 1

    def test_get(self):
        lru = LRUCache(3)
        self._put(lru)
        assert lru.get(1) == 10
        assert lru.get(2) == 20
        lru.put(1, 30)
        assert lru.get(1) == 30

    def test_reset(self):
        lru = LRUCache(3)
        self._put(lru)
        lru.reset()
        assert lru.get(1) == -1
        assert lru.get(2) == -1

    def test_put(self):
        lru = LRUCache(3)
        self._put(lru)
        lru.put(1, 54)
        assert lru.get(1) == 54
        assert lru.get(2) == 20

    def test_delete(self):
        lru = LRUCache(3)
        self._put(lru)
        lru.delete(1)
        lru.delete(2)
        assert lru.get(1) == -1
        assert lru.get(2) == -1
        assert lru.get(3) == 40

    def test_less_capacity(self):
        lru = LRUCache(2)
        self._put(lru)
        assert lru.get(1) == -1
        assert lru.get(3) == 40
        self._put(lru)
        assert lru.get(3) == 40
        assert lru.get(2) == 20
        assert lru.get(1) == -1

    def _put(self, lru):
        lru.put(1, 10)
        lru.put(2, 20)
        lru.put(3, 40)

if __name__ == '__main__':
    unittest2.main()
