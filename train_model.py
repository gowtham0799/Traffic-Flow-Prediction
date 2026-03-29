import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

print("🚀 Code started...")

# Load dataset
df = pd.read_excel("data/traffic_data.xlsx")

# Convert datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Feature engineering
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.dayofweek

# Drop datetime
df.drop('datetime', axis=1, inplace=True)

# One-hot encoding
df = pd.get_dummies(df)

# Split data
X = df.drop('traffic_count', axis=1)
y = df['traffic_count']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# ✅ SAVE MODEL
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

# ✅ SAVE COLUMNS
with open("model/columns.pkl", "wb") as f:
    pickle.dump(X.columns.tolist(), f)

print("✅ Model and columns saved successfully!")