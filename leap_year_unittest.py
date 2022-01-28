# -*- coding: utf-8 -*-

import unittest

from leap_year import LeapYear

test_cases = [
    (2017, '2017 is not leap year'),
    (1900, '1900 is century year'),
    (2012, '2012 is leap year'),
    (2000, '2000 is century leap year'),
    
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