"""
Program: assing_level.py
Author: Tony Ehlert
Last date modified: 3/1/2023

The purpose of this program is simulate a switch that is common other programming languages
by using a dictionary.  The dictionary will contain levels as the keys and point numbers as the values.
A function will then be called and have the level passed in and then return the correct point number

The input is a level passed to a function containing the levels and points contained in a dictionary
The output is a print to the console with the corresponding points to the level passed in
"""

def switch_level(level_to_search):
    """
    This function simulates a switch function by search a dictionary for a key matching the level_to_search
    variable passed in, and then returns the corresponding point value if found, else returns a
    "no such level" statement

    :param level_to_search: letter representing a level within the dictionary
    :return: point value based on matching key if found, else string stating no such level found
    """

    level_dict = {
        "N": 50,
        "B": 150,
        "E": 300,
        "A": 500
    }

    return(level_dict.get(level_to_search, "No such level!"))

# driver
if __name__ == "__main__":
    print("Points for level \"N\" = " + str(switch_level("N")) + ", SHOULD BE 50")
    print("Points for level \"B\" = " + str(switch_level("B")) + ", SHOULD BE 150")
    print("Points for level \"E\" = " + str(switch_level("E")) + ", SHOULD BE 300")
    print("Points for level \"A\" = " + str(switch_level("A")) + ", SHOULD BE 500")
    print("Points for level \"M\" = " + str(switch_level("M")) + ", SHOULD BE \"No Such Level!\"")
