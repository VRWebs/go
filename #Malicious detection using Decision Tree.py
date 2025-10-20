#Malicious detection using Decision Tree. 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score, classification_report 
df = pd.read_csv("malicious_urls.csv") 
print("Dataset Shape:", df.shape) 
print(df.head()) 
def extract_features(url): 
return { 
"url_length": len(url), 
"count_digits": sum(c.isdigit() for c in url), 
"count_special": sum(c in ['?','-','=','@','&','%','_'] for c in url), 
"has_https": 1 if url.startswith("https") else 0, 
"has_ip": 1 if any(char.isdigit() for char in url.split("/")[2]) else 0,  # crude IP check 
"count_dot": url.count(".") 
} 
features = df["url"].apply(extract_features) 
X = pd.DataFrame(list(features)) 
y = df["label"] 
print("\nFeature Sample:\n", X.head()) 
X_train, X_test, y_train, y_test = train_test_split( 
X, y, test_size=0.3, random_state=42 
) 
clf = DecisionTreeClassifier(max_depth=10, random_state=42) 
clf.fit(X_train, y_train) 
y_pred = clf.predict(X_test) 
print("\nModel Accuracy:", accuracy_score(y_test, y_pred)) 
print("\nClassification Report:\n", classification_report(y_test, y_pred) 
test_urls = [ 
"http://secure-login-update.com/paypal", 
"https://openai.com/research", 
"http://192.168.1.1/login"
]
test_features = pd.DataFrame([extract_features(u) for u in test_urls]) 
predictions = clf.predict(test_features) 
print("\nTest Predictions:") 
for url, pred in zip(test_urls, predictions): 
    print(f"{url} -> {'Malicious' if pred==1 else 'Benign'}")