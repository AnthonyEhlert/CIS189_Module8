import unittest
from dictionary_update import average_scores

"""
Program: test_average_scores.py
Author: Tony Ehlert
Last date modified: 03/01/2023

The purpose of this program is to test the average_scores function of the dictionary_update.py file 
The input is different unit tests containing different sizes of dictionaries along with the expected results
The output is the number of tests that passed/failed
"""
class MyTestCase(unittest.TestCase):
    def test_average(self):
        # ARRANGE
        self.scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.66666666

        # ACT
        actual = average_scores(self.scores_dict)

        # ASSERT
        self.assertAlmostEqual(expected, actual)

    def test_average_two(self):
        # ARRANGE
        self.scores_dict = {"Test 1": 98, "Test 2": 97}
        expected = 97.5

        # ACT
        actual = average_scores(self.scores_dict)

        # ASSERT
        self.assertAlmostEqual(expected, actual)

    def test_average_five(self):
        # ARRANGE
        self.scores_dict = {"Test 1": 20, "Test 2": 40, "Test 3": 60, "Test 4": 80, "Test 5": 100,}
        expected = 60

        # ACT
        actual = average_scores(self.scores_dict)

        # ASSERT
        self.assertAlmostEqual(expected, actual)

    def test_average_zero(self):
        # ARRANGE
        self.scores_dict = dict()

        # ACT

        # ASSERT
        with self.assertRaises(ValueError):
            average_scores(self.scores_dict)

if __name__ == '__main__':
    unittest.main()
