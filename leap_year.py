class LeapYearRefactored:

    def __init__(self, year):
        self.year = year

    def print_is_leap_year(self):
        # century year divided by 400 is leap year
        if (self.year % 100 == 0 and self.year % 400 == 0):
            return f"{self.year} is century leap year"
        #  divided by 100 means century year (ending with 00)
        if (self.year % 100 == 0):
            return f"{self.year} is century year"
        # year divided by 4 is a leap year
        if (self.year % 4 == 0):
            return f"{self.year} is leap year"
        return f"{self.year} is not leap year"


LeapYear = LeapYearRefactored
