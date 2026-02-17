# 🚚 Food Delivery Time Predictor

**FastAPI + nginx + ML (pickle) + Docker**

A full-stack ML web application that predicts food delivery time based on weather, distance, traffic level, and courier experience.

The project demonstrates a production-style architecture using FastAPI, nginx reverse proxy, and Docker containers

---

# 🚀 Quick start

```bash
git clone <repo>
cd ML-project
docker compose up --build
```

Open in browser:

```
http://localhost
```

---

# 🧠 What this project does

The app predicts delivery time using a trained ML model.

**Inputs:**

* 🌦 Weather
* 📏 Distance (km)
* 🚦 Traffic level
* 🧑‍💼 Courier experience (years)

**Output:**

* ⏱ Estimated delivery time (minutes)

---

# 🏗 Architecture

```
Browser
   ↓
nginx
   ↓
FastAPI backend
   ↓
Pickle ML model
```

## Services

* **Frontend** — HTML/CSS/JS (jQuery)
* **Backend** — FastAPI + Uvicorn
* **Model** — sklearn pickle
* **Proxy** — nginx
* **Orchestration** — Docker Compose

---


## 🧪 Model training

The ML model was trained in:

food_delivery_times.ipynb


The notebook includes:

- data preprocessing  
- feature engineering  
- model training  
- evaluation  
- pickle export  

The trained model used by the API is stored in:

server/artifacts/food_delivery_time_model.pickle

---

# 📦 Project structure

```
ML-project/
│
├── client/           
│   ├── app.html
│   ├── app.js
│   └── app.css
│
├── server/        
│   ├── server.py
│   ├── util.py
│   └── artifacts/
│       ├── columns.json
│       └── food_delivery_time_model.pickle
│
├── nginx/
│   └── default.conf
│
├── Dockerfile.backend
├── Dockerfile.nginx
├── docker-compose.yml
└── README.md
```

## Predict delivery time

```
POST /api/predict_delivery_time
```

**Request body**

```json
{
  "weather": "Clear",
  "distance": 5.2,
  "traffic_level": "medium",
  "courier_experience_yrs": 3
}
```

**Response**

```json
{
  "estimated_time_min": 28.5
}
```

---

# 🧪 Development workflow

After changing backend code:

```bash
docker compose restart backend
```

After changing frontend:

```bash
docker compose restart nginx
```

