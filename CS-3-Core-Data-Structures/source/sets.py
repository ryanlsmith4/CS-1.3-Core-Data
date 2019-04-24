from hashtable import HashTable

class Set(object):
    def __init__(self, elements = None):
        self.hashtable = HashTable()
        if elements is not None:
            for element in elements:
                self.add(element)

    def __repr__(self):
        return 'Set: {!r}'.format(self.hashtable.keys())

    def size(self):
        ''' Returns the size property of the hashtable
        '''
        return self.hashtable.size

    def contains(self, element):
        ''' Returns True if item is in the set
            False otherwise
        '''
        return self.hashtable.contains(element)

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
        new_set = Set(other_set.hashtable.keys())        # new_set = other_set
        old_set =  self.hashtable.items()
        for element in old_set:
            new_set.add(element)

        return new_set



def test_set():
    set1 = Set(['cat', 'dog', 'fish'])
    set2 =  Set(['green', 'blue', 'dog'])
    set1.add('cat')
    set1.add('dog')
    set1.add('goat')
    new = set1.union(set2)

    print(set1)
    print(new)


if __name__ == '__main__':
    test_set()