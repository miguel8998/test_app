import unittest

from weather.helper.utils import wind_deg_to_text


class TestWindDegToText(unittest.TestCase):
    """Unit tests to check wind direction to text functionality works"""

    def test_standard_wind_deg(self):
        wind_direction = wind_deg_to_text(60)
        self.assertTrue(wind_direction == 'North Easterly')

    def test_wind_deg_0(self):
        wind_direction = wind_deg_to_text(0)
        self.assertTrue(wind_direction == 'Northerly')

    def test_wind_deg_360(self):
        wind_direction = wind_deg_to_text(360)
        self.assertTrue(wind_direction == 'Northerly')

    def test_wind_deg_greater_than_360(self):
        wind_direction = wind_deg_to_text(500)
        self.assertTrue(wind_direction == 'South Easterly')

    def test_wind_deg_less_than_0(self):
        wind_direction = wind_deg_to_text(-45)
        self.assertTrue(wind_direction == 'North Westerly')


if __name__ == '__main__':
    unittest.main()
