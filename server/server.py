from fastapi import FastAPI
from . import util

from starlette.middleware.cors import CORSMiddleware

from pydantic import BaseModel

class DeliveryTimeRequest(BaseModel):
    weather: str
    distance: float
    traffic_level: str
    courier_experience_yrs: float

app = FastAPI()

util.load_saved_artifacts()

traffic_mapping = {"low": 0, "medium": 1, "high": 2}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # разрешаем все домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_weather")
def get_weather():
    return {"weather": util.get_weather()}

@app.get("/get_traffic")
def get_traffic():
    return {"traffic": util.get_traffic()}

@app.post("/predict_delivery_time")
def predict_delivery_time(data: DeliveryTimeRequest):
    traffic_num = traffic_mapping.get(data.traffic_level.lower())
    if traffic_num is None:
        return {"error": "traffic_level должен быть 'low', 'medium' или 'high'"}

    estimated_time = util.get_estimated_time(
        weather=data.weather,
        distance=data.distance,
        traffic_level=traffic_num,
        courier_experience_yrs=data.courier_experience_yrs
    )

    return {"estimated_time_min": estimated_time}