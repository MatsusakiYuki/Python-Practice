# Author: Anni Li,
# Student ID: 30269776
# Start Date: Apr 6
# Last Modification date: Apr 12
# Description:
# This program is designed to do the following things--
# 1. Take in a list of NerdScore
# 2. Report errors if input is not provided in correct type or range.
# 3. Allocate the scores into corresponding Nerd classes based on the specific range of score.
# 4. Count the total number of users in different classes.
# 5. Export the total number of users in each class as a list.



def countStudentClass(studentScore_list):
    if len(studentScore_list) < 1:
        print("Please add at least 1 item into the list")
        return 0

    nerdCount_list = [0] * 7  # intialize the output list

    # Please write your own program here
    for s in studentScore_list:
        if str(s).isdigit() == False:  # check if the score input is integer
            print("Please put in an integer")
        elif s < 0:  # check if the score input is positive
            print("Please put in positive number")

    for s in studentScore_list:
        if s >= 0 and s < 1:  # Count for Nerdlite
            nerdCount_list[0] += 1

        elif s >= 1 and s < 10:  # Count for Nerdling
            nerdCount_list[1] += 1

        elif s > 10 and s < 100:  # Count for Nerdlinger
            nerdCount_list[2] += 1

        elif s >= 100 and s < 500:  # Count for Nerd
            nerdCount_list[3] += 1

        elif s >= 500 and s < 1000:  # Count for Nerdington
            nerdCount_list[4] += 1

        elif s >= 1000 and s < 2000:  # Count for Nerdrometa
            nerdCount_list[5] += 1

        elif s >= 200:  # Count for Nerd Supreme
            nerdCount_list[6] += 1

    return nerdCount_list


if __name__ == '__main__':

    # test cases
    # studentScore_list = []  #
    studentScore_list = [-1, 76, 1300, 600]  # output should be [0, 0, 2, 0, 1, 1, 0]

    try:
        print(countStudentClass(studentScore_list))

    except e:
        print(e)
        raise
