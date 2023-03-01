"""
Program: dictionary_update.py
Author: Tony Ehlert
Last date modified: 03/01/2023

The purpose of this program is ask a user for the number of test scores they want to enter, then prompt the user
for the scores equal to the amount of the number of scores they want to store. Then place the scores in a dictionary
which then gets passed to another function that calculates the average fo the scores

The input is a number indicating the total number of scores to be stored and the scores to be stored
The output is the calculated average of the scores printing to the console
"""


def get_test_scores():
    """
    This function prompts a user for the number of scores they would like to enter and then prompts them
    for the scores.  After the number of scores retrieved equals the number of scores input by the user, the
    scores are then placed inside a dictionary

    :return: a dictionary containing the test scores obtained from user input
    """

    # create an empty dictionary that will be used to store scores
    scores_dict = dict()

    # creation of boolean variable to track valid input
    valid_input = False

    while (not valid_input):
        try:
            # prompt user for number of scores and convert to an integer
            num_of_scores = int(input("Please enter the number of scores you would like to enter: "))

            # if statement to ensure a non-negative number was entered
            if (num_of_scores > 0):
                valid_input = True
            else:
                print("Invalid Entry!")
        except ValueError:
            print("Invalid entry!")

    # reset valid_input variable to False
    valid_input = False

    # create score_count variable to use for key in dictionary
    score_count_int = 0

    # while loop to prompt user for scores
    while ((len(scores_dict) < num_of_scores)):

        try:
            score_input = int(input("Please enter a score: "))

            # if statement to ensure valid range was entered
            if (0 < score_input < 101):
                score_count_int += 1

                # add score to dictionary with key representing score count
                scores_dict.update({f"Score {score_count_int}": score_input})
            else:
                print("Invalid Entry!")
        except ValueError:
            print("Invalid Entry!")

    return scores_dict


def average_scores(scores_dict):
    """
    This function accepts a dictionary object containing scores and then calculates the average of the scores
    and returns the calculated average

    :param scores_dict: a dictionary of scores
    :return: calculated average of the scores
    """

    # create variable to hold cumulative total of scores
    total_of_scores = 0

    # loop through dictionary to get each score and add to total_of_scores
    for key, value in scores_dict.items():
        total_of_scores += value

    # calculate the average of the scores
    calc_average = (total_of_scores / len(scores_dict))

    # return the calculated value
    return calc_average


# driver
if __name__ == "__main__":
    scores_dict = get_test_scores()
    scores_dict_avg = average_scores(scores_dict)
    print(f"The average of the scores is {scores_dict_avg}")
