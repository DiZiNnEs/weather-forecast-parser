from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

import dotenv
import os

dotenv.load_dotenv()

owm = OWM(os.getenv("WEATHER_API_KEY"))
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

w.detailed_status()         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity()        # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain()                    # {}
w.heat_index()              # None
w.clouds()                  # 75

# Will it be clear tomorrow at this time in Milan (Italy) ?
forecast = mgr.forecast_at_place('Milan,IT', 'daily')
answer = forecast.will_be_clear_at(timestamps.tomorrow())