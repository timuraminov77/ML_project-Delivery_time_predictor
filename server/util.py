import json
import pickle
import numpy as np
from pathlib import Path

__weather = None
__traffic = ["low", "medium", "high"]
__data_columns = None
__model = None

BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"

def load_saved_artifacts():
    print("Loading saved artifacts...")
    global __weather, __data_columns, __model

    with open(ARTIFACTS_DIR / "columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]

    __weather = [c for c in __data_columns if c.startswith("weather_")]

    with open(ARTIFACTS_DIR / "food_delivery_time_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Loading saved artifacts...done")



weather_mapping = {
    "weather_clear": "Clear",
    "weather_foggy": "Foggy",
    "weather_rainy": "Rainy",
    "weather_snowy": "Snowy",
    "weather_windy": "Windy"
}

def get_weather():
    return [weather_mapping[w] for w in (__weather or []) if w in weather_mapping]


def get_traffic():
    return __traffic

weather_reverse_mapping = {
    "Clear": "weather_clear",
    "Foggy": "weather_foggy",
    "Rainy": "weather_rainy",
    "Snowy": "weather_snowy",
    "Windy": "weather_windy"
}

def get_estimated_time(weather, distance, traffic_level, courier_experience_yrs):

    try:
        weather_col = weather_reverse_mapping.get(weather)
        loc_index = __data_columns.index(weather_col) if weather_col else -1
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    print(x)
    # числовые признаки
    x[0] = distance
    x[1] = traffic_level
    x[2] = courier_experience_yrs

    # one-hot для погоды
    if loc_index >= 0:
        x[loc_index] = 1

    print(x)
    # предсказание через загруженную модель
    return round(__model.predict([x])[0], 2)

if __name__ == '__main__':
    print(1)
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Ejipura', 1000, 2, 2))