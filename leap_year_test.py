import pytest
from leap_year import LeapYear

from leap_year_unittest import test_cases, is_leap_year

class TestLeapYear:

    @pytest.mark.parametrize('year expected'.split(), test_cases)
    def test_get_year(self, year, expected):
        leap_year = is_leap_year(year)
        assert expected == leap_year.print_is_leap_year()