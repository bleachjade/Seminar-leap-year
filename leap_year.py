from lib2to3.pytree import LeafPattern

# can use test_answer and get leap year to get real output first before 
# creating test cases

test_answer = [
    (1943, '1995 is not leap year'),
    (1045, '1000 is century year'),
    (1234, '1992 is leap year'),
    (3283, '3200 is century leap year'),
    
    (1932, '1999 is not leap year'),
    (1312, '1300 is century year'),
    (1800, '1800 is leap year'),
    (1079, '1600 is century leap year'),
    
    (2231, '2010 is not leap year'),
    (1022, '1800 is century year'),
    (2400, '2400 is leap year'),
    (1186, '1200 is century leap year'),
    ]

class LeapYearRefactored:
    def __init__(self, year):
        self.year = year

    def print_is_leap_year(self):
        # A leap year is a century year divided by 400.
        if (self.year % 100 == 0 and self.year % 400 == 0):
            return f"{self.year} is century leap year"
        # Divided by 100, the year is referred to as a century year (ending with 00)
        if (self.year % 100 == 0):
            return f"{self.year} is century year"
        # A leap year is a year divided by 4.
        if (self.year % 4 == 0):
            return f"{self.year} is leap year"
        return f"{self.year} is not leap year"

    def get_is_leap_year(year):
        # A leap year is a century year divided by 400.
        if (year % 100 == 0 and year % 400 == 0):
            print(f"{year} is century leap year")
            pass
        # Divided by 100, the year is referred to as a century year (ending with 00)
        if (year % 100 == 0):
            print(f"{year} is century year")
            pass
        # A leap year is a year divided by 4.
        if (year % 4 == 0):
            print(f"{year} is leap year")
            pass
        print(f"{year} is not leap year")

LeapYear = LeapYearRefactored

for test in test_answer:
    (year, answer) = test
    LeapYear.get_is_leap_year(year)
