#Spam detection using logistic regression 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import classification_report 
df = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']] 
df.columns = ['label', 'message'] 
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1}) 
X_train, X_test, y_train, y_test = train_test_split( 
df['message'], df['label_num'], test_size=0.2, random_state=42, 
stratify=df['label_num'] 
) 
vectorizer = CountVectorizer() 
X_train_vec = vectorizer.fit_transform(X_train) 
X_test_vec = vectorizer.transform(X_test) 
model = LogisticRegression(max_iter=1000) 
model.fit(X_train_vec, y_train) 
y_pred = model.predict(X_test_vec) 
print(classification_report(y_test, y_pred)) 