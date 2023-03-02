import array as arr

"""
Program: sort_and_search_array.py
Author: Tony Ehlert
Last date modified: 3/1/2023

The purpose of this program is to create an array and call a sort function to sort the array and call a search function
to search the array for a matching object

The input is a hard coded list/array
The output is a print to the console of the results of the function calls
"""


def search_array(array_to_search, item_to_find):
    """
    This function searches an array that is passed in for the matching value that is also passed in
    and returns the index if a match is found, else returns -1 indicating no match was found

    :param array_to_search: list to be converted to an array
    :param item_to_find: item to search the list/array for
    :return: index value of match found, else -1
    """

    try:
        return array_to_search.index(item_to_find)
    except ValueError:
        return -1


def sort_array(array_to_sort):
    """
    This function sorts the array and returns it

    :param array_to_sort: array to be sorted
    :return: sorted array containing the items in the list

    A return statement was included because there is no .sort() for arrays like there is lists
    so the array that was passed in had be to sorted using the sorted() method and then returned a new array
    """

    return sorted(array_to_sort)


if __name__ == "__main__":
    # create an array
    int_array = arr.array('i', [1, 3, 2])

    # create a variable to hold the item to be searched for
    search_item = 1

    # call of the search_array function
    if (search_array(int_array, search_item) == -1):
        print(f"Item \'{search_item}\' was not found in the array.")
    else:
        print(f"\'{search_item}\' was found at index: " + str(search_array(int_array, search_item)))

    # call of the sort_array function
    array_after_sorting = sort_array(int_array)
    print("Array after sorting: " + str(array_after_sorting))
