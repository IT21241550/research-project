import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load cleaned data
data = pd.read_csv('../data/processed/flood_data_cleaned.csv')

# Split features and labels
X = data[['Rainfall(mm)', 'River Level(m)']]
y = data['Flood Occurrence']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'flood_model.pkl')
print("Model saved to flood_model.pkl")
