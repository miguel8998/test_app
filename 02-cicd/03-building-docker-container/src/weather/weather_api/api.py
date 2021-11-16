# pyowm is the open weather api client, use ide and docs to find  methods https://openweathermap.org/api
# to look at client class import pyowm.weatherapi25.weather.Weather
import pyowm
from pyowm.exceptions.api_response_error import NotFoundError, UnauthorizedError, APIResponseError

# allows for conversion from degrees to wind direction
from weather.helper.utils import wind_deg_to_text


class WeatherApiWrapper:
    """
    Wraps pyown in a facade
    """

    def __init__(self, options):
        """An object constructor , called when an object is instantiated"""
        api_key = options['api_key']
        if api_key:
            self.client = pyowm.OWM(options['api_key'])
        else:
            # if there is no api_key we should raise an exception
            raise WeatherApiException("No api key found, exiting")

    def _query_location(self, location):
        """Accepts a  location string e.g London,GB and returns a weather dict, is a private method"""
        location_details = self.client.weather_at_place(location)
        return location_details.get_weather()

    def get_current_weather_at_location(self, location, temperature_unit, wind_unit):
        """
        Gets current weather status at a specific location
        returns a dict of form
        {'status': 'Clouds', 'icon_url': 'http://openweathermap.org/img/w/04d.png', 'temp': 14.32, 'temp_max': 15.0,
         'temp_min': 12.78, 'temp_kf': None}
        """
        try:
            weather_location = self._query_location(location)

        # this method can throw exceptions, catch them and deal with them cleanly
        except (NotFoundError, UnauthorizedError) as e:
            return {'errors': [e]}

        # initialise weather dicitionary
        weather_dict = {
            "status": weather_location.get_status(),
            "icon_url": weather_location.get_weather_icon_url()
        }

        try:
            # get_temperature retrieves a dictionary, so we can append this to ours to avoid too many keys!
            weather_dict.update(weather_location.get_temperature(temperature_unit))

            ## extra code
            weather_dict.update(weather_location.get_wind(wind_unit))
            weather_dict.update({"wind_sector": wind_deg_to_text(weather_dict['deg'])})

        except APIResponseError as e:
            return {'errors': [e]}
        return weather_dict

    ## extra code
    def get_current_weather_at_coordinates(self, longtitude, latitude, unit):
        """Gets the current weather at a specified longitude and latitude"""
        try:
            forecast = self.client.weather_at_coords(latitude, longtitude)
            weather_location = forecast.get_weather()
        except (ValueError, UnauthorizedError) as e:
            return {'errors': [e]}
        weather_dict = {
            "status": weather_location.get_status(),
            "icon_url": weather_location.get_weather_icon_url(),

        }
        weather_dict.update(weather_location.get_temperature(unit))
        return weather_dict
    ##

class WeatherApiException(Exception):
    """Generic weather api exception"""
    pass
