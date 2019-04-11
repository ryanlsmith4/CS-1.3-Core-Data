#!python
import re
import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # Clean the text to remove special chars and white space
    clean_text = re.sub('[^A-Za-z0-9]+', '', text).lower()
    # return is_palindrome_iterative(clean_text)
    return is_palindrome_recursive(clean_text)


def is_palindrome_iterative(text):
    # implement the is_palindrome function iteratively here
    right_index = len(text) - 1
    left_index = 0
    while left_index <= right_index:
        # if !text[left_index].isAlpha():
        #     left_index += 1
        # if !text[right_index].isAlpha():
        #     right_index -= 1
        if text[left_index] == text[right_index]:
            left_index += 1
            right_index -= 1
        else:
            return False
    return True

def is_palindrome_recursive(text, left=0, right=None):
    # implement the is_palindrome function recursively here
    if right == None:
        right = len(text) - 1
    if left >= right: # This means we have a palindrome
        return True
    if text[right] == text[left]:
        return is_palindrome_recursive(text, left + 1, right - 1)
    else:
        return False

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


# print(is_palindrome_iterative('AAAAZAAA'))
# print(is_palindrome_iterative('BB'))
# print(is_palindrome_iterative('race fast safe car'))
# print(is_palindrome_iterative('..dog.. go..d? 2132312 @#$%%%'))
# print(is_palindrome('No! on'))
# print(is_palindrome('race fast safe car'))
# print(is_palindrome('AAAAZAAA'))

if __name__ == '__main__':
    main()
