#!python

from sets import Set

import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        set = Set([4,5,6,7])
        assert set.size() == 4
        set.add(8)
        assert set.size() == 5

    def test_size(self):
        set = Set(['cat', 'dog', 'fish'])
        assert set.size() == 3

    def test_contains(self):
        set = Set(['cat', 'dog', 'fish'])
        set.contains('cat') == True  # should return true
        set.contains('ORANGES') == False # should return false

    def test_add(self):
        set = Set()
        set.add('fish')
        set.contains('fish') == True
        set.add('orange')
        set.contains('orange') == True

    def test_remove(self):
        set = Set(['cat', 'dog', 'fish'])
        assert set.size() == 3 # original length
        set.remove('cat')
        assert set.size() == 2 # should now be 2

    def test_union(self):
        set1 = Set(['cat', 'dog', 'fish'])
        assert set1.size() == 3
        set2 = Set(['orange', 'blue', 'green', 'dog'])
        set3 = set1.union(set2)
        assert set3.size() == 6
