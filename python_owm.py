from typing import (
    List,
)

from pyowm import OWM

import dotenv
import os

dotenv.load_dotenv()

owm = OWM(os.getenv("WEATHER_API_KEY"))
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=52.5244, lon=13.4105)
print()


def current_weather():
    return {
        'Clouds': one_call.current.clouds,
        'Humidity': one_call.current.humidity,
        'Status': one_call.current.status,
        'Detailed status': one_call.current.detailed_status,
        'Visibility distance': one_call.current.visibility_distance,
        'Temperature': one_call.current.temp,
        'Weather_icon_name': one_call.current.weather_icon_name,
    }


def forecast_daily() -> List:
    weather = []
    day = 1
    for every_weather in range(0, 7):
        weather_dict = {
            f'Weather information for day {day} ': {'Clouds': one_call.forecast_daily[every_weather].clouds,
                                                    'Humidity': one_call.forecast_daily[every_weather].humidity,
                                                    'Status': one_call.forecast_daily[every_weather].status,
                                                    'Detailed status': one_call.forecast_daily[
                                                        every_weather].detailed_status,
                                                    'Visibility distance': one_call.forecast_daily[
                                                        every_weather].visibility_distance,
                                                    'Temperature': one_call.forecast_daily[
                                                        every_weather].temperature().get("day",
                                                                                         None),
                                                    'Weather_icon_name': one_call.forecast_daily[
                                                        every_weather].weather_icon_name
                                                    }
        }
        day += 1
        weather.append(weather_dict)

    return weather


for print_ in forecast_daily():
    print(print_)
