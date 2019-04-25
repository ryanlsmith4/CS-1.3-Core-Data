from hashtable import HashTable

class Set(object):
    def __init__(self, elements = None):

        self.hashtable = HashTable()

        if elements is not None:
            for element in elements:
                self.add(element)

    def __repr__(self):

        return 'Set: {!r}'.format(self.hashtable.keys())

    def __iter__(self):

        for item in self.hashtable.keys():

            yield item

    def contains(self, element):
        ''' Returns True if item is in the set
            False otherwise
        '''

        return self.hashtable.contains(element)

    def size(self):
        ''' Returns the size property of the hashtable
        '''

        return self.hashtable.size

    def add(self, element):
        '''Only adds an element if the element doesn't already exist in the set
        '''
        return self.hashtable.set(element)


    def remove(self, element):
        '''Removes the element if it exist Raises Key error if Item doesn't'''

        return self.hashtable.delete(element)

    def union(self, other_set):
        '''Returns a new set that contains the contents of both unique sets
            Ignoring the duplicates
        '''
        union_set = Set(other_set.hashtable.keys())  # union_set = other_set
        old_set =  self.hashtable.keys()
        for element in old_set:
            union_set.add(element)

        return union_set

    def intersection(self, other_set):
        ''''''
        intersection_set = Set()

        if self.size() >= other_set.size():
            larger_set = Set(self.hashtable.keys())
            smaller_set = self
        else:
            larger_set = self
            smaller_set = Set(other_set.hashtable.keys())

        for item in smaller_set:

            if larger_set.contains(item):
                intersection_set.add(item)

        return intersection_set

    def difference(self, other_set):

        difference_set = Set()

        for item in self.hashtable.keys():

            if not other_set.hashtable.contains(item):
                difference_set.add(item)

        return difference_set
    
    def is_subset(self, other_set):
        ''''''
        for items in self:

            if not self.contains(items):
                return False
            
        return True



def test_set():
    set1 = Set(['cat', 'dog', 'fish'])
    set2 =  Set(['green', 'blue', 'fish', 'orange'])
    new = set1.is_subset(set2)
    new2 = set1.difference(set2)

    print(new2)
    print(new)


if __name__ == '__main__':
    test_set()