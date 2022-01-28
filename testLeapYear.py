import pytest


def leap_year(year):
    # A leap year is a century year divided by 400.
    if (year % 100 == 0 and year % 400 == 0):
        return f"{year} is century leap year"
    # Divided by 100, the year is referred to as a century year (ending with 00)
    if (year % 100 == 0):
        return f"{year} is century year"
    # A leap year is a year divided by 4.
    if (year % 4 == 0):
        return f"{year} is leap year"
    return f"{year} is not leap year"


class TestLeapYear:
    def test_century_year(self):
        assert leap_year(2000) == "2000 is century year and leap year"

    def test_leap_year(self):
        assert leap_year(1984) == "1984 is leap year"
