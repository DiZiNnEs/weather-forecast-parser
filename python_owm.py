from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

import dotenv
import os

dotenv.load_dotenv()

owm = OWM(os.getenv("WEATHER_API_KEY"))
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=52.5244, lon=13.4105)

a = one_call.forecast_hourly[3].wind().get('speed', 0)
print(a)