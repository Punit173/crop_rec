# Crop Recommendation System

A web-based crop recommendation system that suggests suitable crops based on various environmental and soil parameters.

## Features

- Input soil parameters (N, P, K content)
- Input environmental conditions (temperature, humidity, pH, rainfall)
- Get crop recommendations based on the input parameters
- Modern and responsive user interface
- Real-time predictions using machine learning

## Setup Instructions

1. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

4. Open your web browser and navigate to:

```
http://localhost:5000
```

## Input Parameters

- Nitrogen (N) Content: 0-140
- Phosphorus (P) Content: 0-140
- Potassium (K) Content: 0-140
- Temperature (°C): 0-50
- Humidity (%): 0-100
- pH Value: 0-14
- Rainfall (mm): 0-300

## Technologies Used

- Backend: Python Flask
- Frontend: HTML, CSS, JavaScript
- Machine Learning: scikit-learn
- Data Processing: pandas, numpy
