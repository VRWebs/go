#Finding domain similarity between malicious URLs 
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
df = pd.read_csv("malicious_urls.csv") 
urls = df['url'].head(10).tolist() 
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3, 5)) 
tfidf_matrix = vectorizer.fit_transform(urls) 
similarity_matrix = cosine_similarity(tfidf_matrix) 
print("Similarity between malicious URLs:\n") 
for i in range(len(urls)): 
for j in range(i+1, len(urls)): 
print(f"Similarity({urls[i]} , {urls[j]}) = {similarity_matrix[i][j]:.2f}") 