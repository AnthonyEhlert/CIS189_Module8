"""
Program: set_membership.py
Author: Tony Ehlert
Last date modified: 03/01/2023

The purpose of this program is to create a set and a test value and pass them into a function
that returns a boolean indicating if the test value is in the set

The input is a set of values and a test value
The output is a print to the console indicating if the test value was in the set
"""


def in_set(set_to_search, value_to_search):
    """
    This method accepts a predefined set and a value, then searches if the value is
    contained within the set using keyword "in".  If it is in the set, return True, else return False

    :param set_to_search: variable with a value to search for a match within set
    :param value_to_search: set of values to be searched
    :return: boolean indicating if value is in set
    """

    return (value_to_search in set_to_search)


if __name__ == '__main__':
    test_set = {"blue", "red", "green", "purple"}
    test_value = "yellow"
    match = in_set(test_set, test_value)
    if (match):
        print(f"The value '{test_value}' is in the set {test_set}")
    else:
        print(f"The value '{test_value}' is not in the set {test_set}")
