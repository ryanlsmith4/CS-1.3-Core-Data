import unittest

# list_1 = ["fish", "cow", "chicken", "cow", "fish", "fish", "fish", "tater"]
# list_2 = ["cow", "orange", "fish", "flight", "chicken", "fish"]

class Redact_words_test(unittest.TestCase):
    def test_redact_len_words(self):
        list_1 = ["fish", "cow", "chicken", "cow", "fish", "fish", "fish", "tater"]
        list_2 = ["cow", "orange", "fish", "flight", "chicken", "fish"]
        result = redact_words(list_1, list_2)
        assert len(result) == 1

    def test_redact_certain_words(self):
        list_1 = ["fish", "cow", "chicken", "cow", "fish", "fish", "fish", "tater"]
        list_2 = ["cow", "orange", "fish", "flight", "chicken", "fish"]
        result = redact_words(list_1, list_2)
        assert "cow" not in result
        assert "fish" not in result

    def test_one_word(self):
        words = ["lettuce"]
        banned_words = ["lettuce"]
        result = redact_words(words, banned_words)
        assert len(result) == 0



def redact_words(words, banned_words):
    '''O(n)'''
    redacted_sentence = []
    set_of_banned = set(banned_words) # O(m)
    for word in words: # O(n)
        if word not in set_of_banned: # O(1) Set are constant time look up
            redacted_sentence.append(word)
    return redacted_sentence

# if __name__ == '__main__':
#     # redact_words(list_1, list_2)
