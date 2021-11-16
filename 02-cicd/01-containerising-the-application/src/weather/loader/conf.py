import yaml


def read_yaml_file():
    """
    Load configuration from yaml file
    """
    config_file = open("weather/config.yaml")
    parsed_yaml = yaml.load(config_file, Loader=yaml.FullLoader)
    if validate_config(parsed_yaml):
        return parsed_yaml
    else:
        # if it is not yaml we are not loading!
        print("Config parsing has failed")
        exit(1)


def validate_config(config):
    """
    Check for mandatory keys and values
    """
    if (
            'api_key' not in config 
            or 'temperature_unit' not in config 
            or 'wind_unit' not in config
            ):
        return False
    if config['temperature_unit'] not in ['celsius', 'kelvin', 'fahrenheit']:
        return False
    if config['wind_unit'] not in ['miles_hour']:
        return False
    return True
