from typing import (
    List,
)

from pyowm import OWM

import dotenv
import os

dotenv.load_dotenv()

owm = OWM(os.getenv("WEATHER_API_KEY"))
mgr = owm.weather_manager()
one_call_api = mgr.one_call_api(lat=52.5244, lon=13.4105)


def current_weather():
    return {
        'Clouds': one_call_api.current.clouds,
        'Humidity': one_call_api.current.humidity,
        'Status': one_call_api.current.status,
        'Detailed status': one_call_api.current.detailed_status,
        'Visibility distance': one_call_api.current.visibility_distance,
        'Temperature': one_call_api.current.temp,
        'Weather_icon_name': one_call_api.current.weather_icon_name,
    }


def forecast_daily() -> List:
    weather = []
    day = 1
    for every_weather in range(0, 7):
        weather_dict = {
            'Clouds': one_call_api.forecast_daily[every_weather].clouds,
            'Humidity': one_call_api.forecast_daily[every_weather].humidity,
            'Status': one_call_api.forecast_daily[every_weather].status,
            'Detailed status': one_call_api.forecast_daily[
                every_weather].detailed_status,
            'Visibility distance': one_call_api.forecast_daily[
                every_weather].visibility_distance,
            'Temperature': one_call_api.forecast_daily[
                every_weather].temperature().get("day",
                                                 None),
            'Weather icon name': one_call_api.forecast_daily[
                every_weather].weather_icon_name

        }
        day += 1
        weather.append(weather_dict)

    return weather


def output_weather():
    for weekly_weather in forecast_daily():
        print('-------------------------------------------------------------')
        print('Clouds: ', weekly_weather['Clouds'])
        print('Humidity: ', weekly_weather['Humidity'])
        print('Status: ', weekly_weather['Status'])
        print('Detailed status: ', weekly_weather['Detailed status'])
        print('Visibility distance: ', weekly_weather['Visibility distance'])
        print('Temperature: ', weekly_weather['Temperature'])
        print('Weather icon name: ', weekly_weather['Weather icon name'])
        print('-------------------------------------------------------------')


output_weather()
