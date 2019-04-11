#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    index = find_index(text, pattern)
    if index is not None:
        return True
    else:
        return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    # Catch edge case of no text
    if pattern == '':
        return 0
    for i in range(len(text) - len(pattern) + 1):
        # Patten Found
        if text[i] == pattern[0]:
            matched_pattern =  True
            # check that the pattern found follow the index
            for j in range(1, len(pattern)):
                if text[i + j] != pattern[j]:
                    matched_pattern = False
                    break
            if matched_pattern:
                return i
    return None
#
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    index = find_index(text, pattern)
    index_list = []
    if pattern == '':
        for i in range(len(text)):
            index_list.append(i)
        return index_list
    if index == None:
        return index_list

    index_list.append(index)
    # print(index)
    for i in range(index + 1, len(text) - len(pattern) + 1):
        if text[i] == pattern[0]:
            matched_pattern = True
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    matched_pattern = False
                    break
            if matched_pattern:
                index_list.append(i)
    return index_list

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")

# assert find_all_indexes('abc', '') == [0, 1, 2]  # all strings contain empty string
# assert find_all_indexes('abc', 'a') == [0]  # single letters are easy
# assert find_all_indexes('abc', 'b') == [1]
# assert find_all_indexes('abc', 'c') == [2]
# assert find_all_indexes('abc', 'ab') == [0]  # multiple letters are harder
# assert find_all_indexes('abc', 'bc') == [1]
# assert find_all_indexes('abc', 'abc') == [0]  # all strings contain themselves
# assert find_all_indexes('aaa', 'a') == [0, 1, 2]  # multiple occurrences
# assert find_all_indexes('aaa', 'aa') == [0, 1]
# assert find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences




print(find_all_indexes('abcabcabc', 'abc'))
#
# if __name__ == '__main__':
#     main()
