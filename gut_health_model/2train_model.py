# 2. train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv('gut_health_data.csv')
X = df[['age', 'constipation_freq', 'stress_level', 'water_intake', 'fiber_intake']]
y = df['risk_level']

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

joblib.dump(model, 'gut_health_model.pkl')
print("✅ 模型已保存为 gut_health_model.pkl")