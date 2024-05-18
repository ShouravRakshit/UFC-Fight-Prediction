import os
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Create the directory if it doesn't exist
model_dir = 'backend/todo/ml'
os.makedirs(model_dir, exist_ok=True)

# Generate synthetic data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 5, 7, 9])  # Simple linear relationship y = 2 * X + 1

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
model_path = os.path.join(model_dir, 'linear_regression_model.pkl')
joblib.dump(model, model_path)
print("Model trained and saved successfully!")
