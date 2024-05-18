import joblib
import os
import numpy as np

# Define the path to the model file
model_path = os.path.join(os.path.dirname(__file__), 'linear_regression_model.pkl')

# Load the model
model = joblib.load(model_path)

def predict(input_data):
    # Convert input_data to numpy array and reshape
    input_array = np.array(input_data).reshape(-1, 1)
    # Predict using the model
    predictions = model.predict(input_array)
    return predictions.tolist()
