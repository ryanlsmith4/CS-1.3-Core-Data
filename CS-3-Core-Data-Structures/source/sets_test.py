#!python

from sets import Set

import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        set = Set()
        assert set.size() == 0

    def test_init_with_elements(self):
        set = Set([4,5,6,7])
        assert set.size() == 4

    def test_size(self):
        set = Set(['a', 'b', 'c'])
        assert set.size() == 3

    def test_contains(self):
        set = Set(['a', 'b', 'c'])
        set.contains('a') == True  # should return true
        set.contains('d') == False # should return false

    def test_add(self):
        set = Set()
        set.add('c')
        set.contains('c') == True
        set.add('d')
        set.contains('d') == True

    def test_remove(self):
        set = Set(['a', 'b', 'c'])
        assert set.size() == 3 # original length
        set.remove('a')
        assert set.size() == 2 # should now be 2

    def test_union(self):
        set1 = Set(['a', 'b', 'c'])
        assert set1.size() == 3
        set2 = Set(['d', 'e', 'f', 'b'])
        set3 = set1.union(set2)
        assert set3.size() == 6

    def test_intersection(self):
        set1 = Set(['a', 'b', 'c'])
        set2 = Set(['d', 'e','a', 'c'])
        set3 = set1.intersection(set2)
        assert set3.contains('a') is True
        assert set3.contains('d') is False
        assert set3.contains('e') is False

    def test_difference(self):
        set1 = Set(['a', 'b', 'c', 'd'])
        set2 = Set(['a', 'b', 'c', 'e'])
        set3 = set1.difference(set2)
        set4 = set2.difference(set1)
        assert set3.contains('a') is False
        assert set3.contains('b') is False
        assert set3.contains('c') is False
        assert set3.contains('d') is True
        assert set4.contains('e') is True

    def test_is_subset(self):
        set1 = Set(['a', 'b', 'c', 'd'])
        set2 = Set(['b', 'c'])
        result = set1.is_subset(set2)
        assert result is True


