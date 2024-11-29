from flask import Flask, request, jsonify
import joblib
import os
from utils.preprocessing import preprocess_data

app = Flask(__name__)

# Load the model
model_path = os.path.join('../models', 'flood_model.pkl')
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    rainfall = data.get('rainfall')
    river_level = data.get('river_level')
    
    # Preprocess input
    input_data = preprocess_data(rainfall, river_level)
    prediction = model.predict([input_data])[0]

    result = "High Risk" if prediction == 1 else "Low Risk"
    return jsonify({'Flood Risk': result})

if __name__ == '__main__':
    app.run(debug=True)
