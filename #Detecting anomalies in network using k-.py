#Detecting anomalies in network using k-means 
import pandas as pd 
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans 
from sklearn.metrics import classification_report, accuracy_score 
df = pd.read_csv("network_data.csv")    
print("Dataset shape:", df.shape) 
X = df.drop("label", axis=1) 
y_true = df["label"].apply(lambda x: 0 if x == "normal" else 1)  # 0=normal, 1=anomaly 
scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10) 
y_pred = kmeans.fit_predict(X_scaled) 
import numpy as np 
if sum(y_pred) > len(y_pred) / 2:   # If 1s are majority, flip labels 
y_pred = 1 - y_pred 
print("\nAccuracy:", accuracy_score(y_true, y_pred)) 
print("\nClassification Report:\n", classification_report(y_true, y_pred)) 
# Example: duration, src_bytes, dst_bytes, failed_logins 
test_data = pd.DataFrame([ 
[0, 491, 0, 0],     
 # Likely normal 
[10, 10000, 5000, 5] # Suspicious anomaly 
], columns=["duration","src_bytes","dst_bytes","failed_logins"]) 
test_scaled = scaler.transform(test_data) 
test_pred = kmeans.predict(test_scaled) 
for sample, pred in zip(test_data.values, test_pred): 
print(f"Sample {sample} --> {'Anomaly' if pred==1 else 'Normal'}")