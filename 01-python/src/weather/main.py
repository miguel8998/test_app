#!/usr/bin/python

"""WeatherApp

Uses the weather openapi to display the weather in any location.
Underneath the hood this application uses an openapi library to connect and obtain
data.
The Flask framework is used to host a website that exposes the weather when a location is typed in.
"""

# flask framework imports
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# configuration loader
from weather.loader import conf
# weather api wrapper
from weather.weather_api.api import WeatherApiWrapper


def create_app(config=None):
    """
    Bootstraps Flask application and defines routes for web applications
    """
    # create and configure the app
    app = Flask(__name__)
    # Basic bootstrap html / header stuffs
    Bootstrap(app)
    options = conf.read_yaml_file()

    # define actions for a GET or POST using / uri
    @app.route('/', methods=['GET', 'POST'])
    def index():

        # initialise variables
        weather = {}
        coord_weather = {}
        location = ""

        if request.method == "POST":
            # get location that the user has entered
            try:
                location = request.form['location']

            except:
                # in these cases we have no choice but to exit
                print("Unable to get location in request, something has gone badly wrong!")
                exit(1)

            if location:
                # for a api wrapper object
                weather_api_wrapper = WeatherApiWrapper(options)

                # return a map with weather at the desired location
                weather = weather_api_wrapper.get_current_weather_at_location(location, options['temperature_unit'])

                # TODO add in ability to get wind direction


                # if errors are found return a 500 page and carry on
                if 'errors' in weather:
                    return render_template('500.html', errors=weather.get('errors'))

            # TODO add in ability to obtain weather from longitude and latitude

        return render_template("index.html", weather=weather, location=location)

    # in cases of generic error return 500
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html', errors=[error]), 500

    return app


# if python runs this file directly load config, launch flask and run!
if __name__ == '__main__':
    conf.read_yaml_file()
    app = create_app(conf)
    app.run()
