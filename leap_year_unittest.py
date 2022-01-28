# -*- coding: utf-8 -*-

import unittest

from leap_year import LeapYear

test_cases = [
    (1998, '1998 is not leap year'),
    (2100, '2100 is century year'),
    (2008, '2008 is leap year'),
    (2800, '2800 is century leap year'),
    
    (1997, '1997 is not leap year'),
    (1000, '1000 is century year'),
    (1988, '1988 is leap year'),
    (2400, '2400 is century leap year'),
    
    (1995, '1995 is not leap year'),
    (1000, '1000 is century year'),
    (1992, '1992 is leap year'),
    (3200, '3200 is century leap year'),
    
    (1999, '1999 is not leap year'),
    (1300, '1300 is century year'),
    (1996, '1996 is leap year'),
    (1600, '1600 is century leap year'),
    
    (2010, '2010 is not leap year'),
    (1800, '1800 is century year'),
    (2004, '2004 is leap year'),
    (1200, '1200 is century leap year'),
    

    (2017, '2017 is not leap year'),
    (1900, '1900 is century year'),
    (2012, '2012 is leap year'),
    (2000, '2000 is century leap year'),
    
    (1996, '1996 is leap year'),
    (1200, '1200 is century leap year'),
    (1958, '1958 is not leap year'),
    (2430, '2430 is not leap year'),

    (1943, '1943 is not leap year'),
    (1045, '1045 is not leap year'),
    (1234, '1234 is not leap year'),
    (3283, '3283 is not leap year'),
    
    (1932, '1932 is leap year'),
    (1312, '1312 is leap year'),
    (1800, '1800 is century year'),
    (1079, '1079 is not leap year'),
    
    (2231, '2231 is not leap year'),
    (1022, '1022 is not leap year'),
    (2400, '2400 is century leap year'),
    (1186, '1186 is not leap year'),
    ]

def is_leap_year(year):
    return LeapYear(year)

class TestLeapYear(unittest.TestCase):
     
    def test_Score(self):
        for testcase in test_cases:
            (year, expected) = testcase
            leap_yeap = is_leap_year(year)
            self.assertEqual(expected, leap_yeap.print_is_leap_year())
 
if __name__ == "__main__":
    unittest.main() 