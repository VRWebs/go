#Logistic Regression to Detect Malicious URLs 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import classification_report, accuracy_score 
data = pd.read_csv("malicious_urls.csv") 
Loads the dataset malicious_urls.csv into a DataFrame called data. 
print(data.head()) 
X = data["url"]   # URL text 
y = data["label"] # 0 = benign, 1 = malicious 
vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(3,5)) 
X_vec = vectorizer.fit_transform(X) 
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, 
random_state=42) 
model = LogisticRegression(max_iter=1000) 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
print("\nModel Accuracy:", accuracy_score(y_test, y_pred)) 
print("\nClassification Report:\n", classification_report(y_test, y_pred)) 
new_urls = [ 
"http://paypal-login-secure.com/update", 
"http://openai.com/research", 
"http://facebook-verification.net/auth" 
] 
new_vec = vectorizer.transform(new_urls) 
predictions = model.predict(new_vec) 
print("\nPrediction on new URLs:") 
for url, label in zip(new_urls, predictions): 
print(f"{url} => {'MALICIOUS' if label == 1 else 'BENIGN'}")