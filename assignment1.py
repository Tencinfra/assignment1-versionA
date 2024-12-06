#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2024
Program: assignment1.py 
Author: Chograb Tenzin
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1 # Adjusts for January and February
    # Calculate day of the week
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    # February depends on leap year
    if month == 2:
        return 29 if leap_year(year) else 28
    # Months with 31 days
    return {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
            4: 30, 6: 30, 9: 30, 11: 30}[month]

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    try:
        year, month, day = map(int, date.split('-'))
        # Ensures month is within valid range
        if not (1 <= month <= 12):
            return False
        # Ensures day is valid for the given month and year
        if not (1 <= day <= mon_max(month, year)):
            return False
        return True
    except ValueError:
        # If parsing fails, the date is invalid
        return False

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    count = 0
    current_date = start_date
    while current_date <= end_date:
        year, month, day = map(int, current_date.split('-'))
        # Increment count if the current date is Saturday or Sunday
        if day_of_week(year, month, day) in ['sat', 'sun']:
            count += 1
        current_date = after(current_date)
    return count

if __name__ == "__main__":
    # Checks for exactly two arguments
    if len(sys.argv) != 3:
        usage()

    # Validates both dates
    start_date, end_date = sys.argv[1], sys.argv[2]
    if not valid_date(start_date) or not valid_date(end_date):
        usage()

    # Ensures start_date is earlier than end_date
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    # Counts weekend days and prints result
    weekends = day_count(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days.")

