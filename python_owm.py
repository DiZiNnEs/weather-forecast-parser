from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

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


def forecast_daily():
    weather = []
    day = 1
    for x in range(0, 7):
        weather_dict = {
            f'Weather information for day {day} ': {f'Clouds: {one_call.forecast_daily[x].clouds}',
                                                    f'Humidity: {one_call.forecast_daily[x].humidity}',
                                                    f'Status: {one_call.forecast_daily[x].status}',
                                                    f'Detailed status: {one_call.forecast_daily[x].detailed_status}',
                                                    f'Visibility distance: {one_call.forecast_daily[x].visibility_distance}',
                                                    f'Temperature: {one_call.forecast_daily[x].temperature().get("day", None)}',
                                                    f'Weather_icon_name: {one_call.forecast_daily[x].weather_icon_name}'},
        }
        day += 1
        weather.append(weather_dict)

    print(weather)


forecast_daily()

# print(current_weather())
