from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

app = Flask(__name__)

# Load and prepare the dataset
def load_data():
    # Sample data - in a real application, you would use a proper dataset
    data = {
    'N': [90, 85, 60, 74, 78, 69, 83, 45, 88, 76, 92, 81, 70, 77, 84, 73, 68, 56, 85, 89, 95, 80, 63, 72, 85, 78, 67, 82, 54, 75, 93, 87, 66, 59, 74, 82, 79, 71, 68, 62],
    'P': [42, 58, 55, 35, 40, 55, 45, 50, 42, 55, 43, 52, 48, 50, 44, 57, 53, 46, 58, 49, 47, 54, 50, 45, 51, 44, 60, 49, 55, 48, 52, 57, 41, 53, 45, 50, 46, 54, 43, 49],
    'K': [43, 41, 44, 39, 41, 57, 50, 48, 43, 45, 47, 42, 46, 40, 49, 44, 43, 41, 46, 48, 50, 44, 42, 43, 47, 49, 41, 46, 45, 48, 42, 43, 49, 41, 48, 46, 44, 47, 43, 50],
    'temperature': [20.87, 21.77, 23.00, 26.27, 20.13, 21.77, 24.27, 26.27, 23.00, 25.13, 22.50, 24.10, 21.60, 25.00, 23.50, 22.20, 24.50, 23.80, 21.90, 25.40, 22.80, 23.50, 24.30, 21.70, 25.20, 22.40, 23.90, 24.00, 22.00, 25.10, 23.80, 21.60, 24.50, 23.30, 22.10, 25.00, 22.90, 24.40, 23.20, 21.80],
    'humidity': [82.00, 86.00, 92.00, 80.00, 83.00, 86.00, 80.00, 80.00, 92.00, 85.00, 84.00, 87.00, 89.00, 81.00, 83.00, 88.00, 85.00, 86.00, 90.00, 82.00, 84.00, 88.00, 91.00, 85.00, 83.00, 87.00, 89.00, 90.00, 82.00, 88.00, 84.00, 86.00, 83.00, 89.00, 87.00, 88.00, 85.00, 86.00, 90.00, 84.00],
    'ph': [6.50, 6.80, 6.30, 6.80, 7.00, 6.50, 6.80, 6.80, 6.30, 6.80, 6.60, 6.40, 6.70, 6.90, 6.50, 6.60, 6.80, 6.70, 6.40, 6.90, 6.50, 6.70, 6.60, 6.80, 6.40, 6.90, 6.50, 6.70, 6.60, 6.40, 6.80, 6.90, 6.50, 6.70, 6.60, 6.90, 6.50, 6.70, 6.60, 6.80],
    'rainfall': [202.93, 226.66, 242.86, 262.76, 262.76, 242.86, 262.76, 262.76, 242.86, 226.66, 215.60, 230.75, 245.80, 260.90, 250.00, 240.30, 255.70, 235.80, 225.90, 260.10, 212.90, 228.60, 240.80, 250.90, 235.70, 220.80, 245.30, 230.40, 220.50, 250.20, 212.30, 240.10, 235.50, 225.60, 230.80, 245.90, 210.60, 225.70, 240.40, 255.60],
    'label': ['rice', 'rice', 'rice', 'rice', 'rice', 'rice', 'rice', 'rice', 'rice', 'rice', 'wheat', 'wheat', 'wheat', 'wheat', 'wheat', 'maize', 'maize', 'maize', 'maize', 'maize', 'barley', 'barley', 'barley', 'barley', 'barley', 'sorghum', 'sorghum', 'sorghum', 'sorghum', 'sorghum', 'millet', 'millet', 'millet', 'millet', 'millet', 'cotton', 'cotton', 'cotton', 'cotton', 'cotton']
    }

    return pd.DataFrame(data)

# Train the model
def train_model():
    df = load_data()
    X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df['label']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = train_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array([[
            float(data['N']),
            float(data['P']),
            float(data['K']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]])
        
        prediction = model.predict(features)[0]
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 