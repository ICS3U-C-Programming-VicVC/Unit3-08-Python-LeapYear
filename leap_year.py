#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 09/16/26
# This program determines whether or not an input year is a leap year

import constants


def main():

    # Getting a year from the user
    year_str = input("Enter a year: ")

    # the try statement will make sure the code safely with invalid user inputs
    try:
        # Converting the year input to an integer
        year_int = int(year_str)

        # This section calculates whether or not the input year is a leap year or not, and displays it back to the user
        if year_int % 4 == 0:

            if year_int % 100 == 0:

                if year_int % 400 == 0:

                    print("{}".format(year_int), constants.IS_LEAP_YEAR)

                else:
                    print("{}".format(year_int), constants.IS_NOT_LEAP_YEAR)

            else:
                print("{}".format(year_int), constants.IS_LEAP_YEAR)

        else:
            print("{}".format(year_int), constants.IS_NOT_LEAP_YEAR)

    # If the try statement fails, it was likely due to the input from the user being invalid
    except:
        print("{}".format(year_str), constants.ERR_MSG)


if __name__ == "__main__":
    main()
