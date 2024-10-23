import unittest
from hw1 import vowel_count, short_lists, ascending_pairs


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1

    def test_vowel_count(self):
        test = "Hello"
        result = vowel_count(test)
        expected = 2
        self.assertEqual(expected, result)


    def test_vowel_count2(self):
        test = "pl"
        result = vowel_count(test)
        expected = 0
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists(self):
        test = [[4], [5], [6, 7], [8, 9, 10]]
        result = short_lists(test)
        expected = [[6, 7]]
        self.assertEqual(expected, result)
    def test_short_lists2(self):
        test = [[4], [5], [6, 7, 8], [8, 9, 10]]
        result = short_lists(test)
        expected = []
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs(self):
        test = [[4], [5], [6, 7], [8, 9, 10]]
        result = ascending_pairs(test)
        expected = [[4], [5], [6,7], [8, 9, 10]]
        self.assertEqual(expected, result)

    def test_ascending_pairs2(self):
        test = [[4], [5], [10, 7], [8, 9, 10]]
        result = ascending_pairs(test)
        expected = [[4], [5], [7, 10], [8, 9, 10]]
        self.assertEqual(expected, result)

    # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





