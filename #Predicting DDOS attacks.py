#Predicting DDOS attacks 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score 
data = { 
'packet_rate': [100, 5000, 200, 7000, 300, 10000, 150, 8000], 
'duration': [1, 0.1, 1.5, 0.05, 1.2, 0.02, 1.1, 0.03], 
'flag_SYN': [0, 1, 0, 1, 0, 1, 0, 1],  # Whether SYN flag is set (1 = yes) 
'is_ddos': [0, 1, 0, 1, 0, 1, 0, 1]   # 1 = DDoS, 0 = Normal 
} 
df = pd.DataFrame(data) 
X = df[['packet_rate', 'duration', 'flag_SYN']] 
y = df['is_ddos'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 
model = RandomForestClassifier() 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
accuracy = accuracy_score(y_test, y_pred) 
print(f"Accuracy: {accuracy * 100:.2f}%") 
sample = pd.DataFrame({'packet_rate': [9000], 'duration': [0.03], 'flag_SYN': [1]}) 
prediction = model.predict(sample) 
print("Prediction for sample traffic:", "DDoS Attack" if prediction[0] == 1 else 
"Normal") 