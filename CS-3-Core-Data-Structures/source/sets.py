from hashtable import HashTable

class Set(object):
    def __init__(self, elements = None):
    """Initialize this set with a hashtable."""
        self.hashtable = HashTable()
        if elements is not None:
            for element in elements:
                self.add(element)

    def size(self):
        ''' Returns the size property of the hashtable
        '''
        return self.hashtable.size

    def contains(self, element):
        return self.hashtable.contains(element)

    def add(self, element):
        if self.hashtable.contains(element) == False:
            return self.hashtable.set(element)
        else:
            break
            # return "Item already in set"
    def remove(self, element):
        return self.hashtable.delete(element)

    def union(self, other_set):
        new_set = Set()
        old_set =  self.hashtable.items()
        for element in old_set:
            new_set.add(element)
        for element in other_set:
            new_set.add(element)



def test_set():


if __name__ == '__main__':
    test_set()