#SVM to Detect Malicious URLs 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score, classification_report 
data = pd.read_csv("malicious_urls.csv")   # dataset: url, label 
X = data["url"] 
y = data["label"] 
vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(3,5)) 
X_vec = vectorizer.fit_transform(X) 
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, 
random_state=42) 
svm_model = SVC(kernel="linear")    
svm_model.fit(X_train, y_train) 
y_pred = svm_model.predict(X_test) 
print("Model Accuracy:", accuracy_score(y_test, y_pred)) 
print("\nClassification Report:\n", classification_report(y_test, y_pred)) 
new_urls = [ 
"http://paypal-login-secure.com/update", 
"http://openai.com/research", 
"http://facebook-verification.net/auth" 
] 
new_vec = vectorizer.transform(new_urls) 
predictions = svm_model.predict(new_vec) 
print("\nPrediction on new URLs:") 
for url, label in zip(new_urls, predictions): 
print(f"{url} => {'MALICIOUS' if label == 1 else 'BENIGN'}")