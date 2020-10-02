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
    for x in range(0, 7):
        print(one_call.forecast_daily[x])


print(current_weather())







