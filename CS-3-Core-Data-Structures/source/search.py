#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # attempts = 0
    if len(array) -1 == index - 1:
        return None
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # implement binary search iteratively here
    if len(array) == 0: # catch empty array
        return None
    half = len(array) // 2 # Look at middle of list
    # keep Track to make sure if the item isn't found we retrun None
    chances = len(array) -1
    while chances != 0:
        if item == array[half]: # Did we find Item first try?
            return half
        elif item < array[half]: # if item is smaller than our first pick
            half = half // 2 # Shrink where we're looking in half
            chances -= 1
        elif item > array[half]: # if item is larger than our first pick
            # Moves the focused item to the right
            half = half + (len(array) - half) // 2
            chances -= 1
    return None

def binary_search_recursive(array, item, left=None, right=None):
    if right == None or left == None: # 1st Check to get the ball rolling
        right = len(array) - 1 # assign where right should begin
        left = 0 # assign where left should begin
        middle = len(array) // 2 # first middle assignment
    else:
        middle = (left + right) // 2 # middle is assigned after first iteration
    if len(array) == 0: # check that array is not none
        return None
    if item == array[middle]: # Does the item match the spot in the array
        return middle
    # check if left and right are equal to return non list items
    if left == right:
        return None
    # item less than current pointer; move pointer to the left
    if item < array[middle]:
        return binary_search_recursive(array, item, left, middle - 1)
    # item greater than current pointer; move pointer to the right
    if item > array[middle]:
        return binary_search_recursive(array, item, middle + 1, right)
