import pandas as pd

# Load raw data
rainfall = pd.read_csv('../data/raw/rainfall_data.csv')
river_level = pd.read_csv('../data/raw/river_level_data.csv')
flood_history = pd.read_csv('../data/raw/flood_history.csv')

# Merge datasets on Date
merged_data = pd.merge(rainfall, river_level, on='Date')
merged_data = pd.merge(merged_data, flood_history, on='Date')

# Save cleaned data
merged_data.to_csv('../data/processed/flood_data_cleaned.csv', index=False)
print("Data preprocessed and saved.")
