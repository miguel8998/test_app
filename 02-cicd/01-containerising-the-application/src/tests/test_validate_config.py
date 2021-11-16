import unittest

from weather.loader.conf import validate_config


class TestValidateConfig(unittest.TestCase):
    """Unit tests to ensure validate_config works correctly"""

    def test_standard_validation(self):
        config = {"temperature_unit": "celsius", 'api_key': "xxx", "wind_unit": "miles_hour"  }
        self.assertTrue(validate_config(config))

    def test_missing_fields_validation(self):
        config = {'api_key': "xxx"}
        self.assertFalse(validate_config(config))

    def test_wrong_temperature_units_validation(self):
        config = {"temperature_unit": "super_celsius", 'api_key': "xxx", "wind_unit": "miles_hour"}
        self.assertFalse(validate_config(config))

    def test_wrong_wind_units_validation(self):
        config = {"temperature_unit": "celsius", 'api_key': "xxx","wind_unit": "super_miles_hour"}
        self.assertFalse(validate_config(config))

if __name__ == '__main__':
    unittest.main()
