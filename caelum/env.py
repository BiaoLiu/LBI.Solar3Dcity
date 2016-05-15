"""Enviroment."""
import os,sys

# WEATHER_DATA_PATH = "d:" + "/weather_data"

WEATHER_DATA_PATH = os.path.dirname(sys.argv[0])+'/weather_data'

SRC_PATH = os.path.dirname(os.path.abspath(__file__))

try:
    os.listdir(WEATHER_DATA_PATH)
except OSError:
    try:
        os.mkdir(WEATHER_DATA_PATH)
    except IOError:
        pass
