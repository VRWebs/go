#Perform regression for doing predictions on diabetes data set  
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import datasets, linear_model 
from sklearn.metrics import mean_squared_error, r2_score 
X, y = datasets.load_diabetes(return_X_y=True) 
X = X[:, np.newaxis, 2] 
X_train, X_test = X[:-20], X[-20:] 
y_train, y_test = y[:-20], y[-20:] 
model = linear_model.LinearRegression() 
model.fit(X_train, y_train) 
m = model.coef_[0] 
b = model.intercept_ 
print(f"Model: y = {m:.3f} · x + {b:.3f}") 
y_pred = model.predict(X_test) 
mse = mean_squared_error(y_test, y_pred) 
r2 = r2_score(y_test, y_pred) 
print(f"Mean squared error: {mse:.2f}") 
print(f"R² score: {r2:.2f}") 
plt.scatter(X_test, y_test, color="black", label="Actual") 
plt.plot(X_test, y_pred, color="blue", linewidth=2, label="Fitted line") 
plt.xlabel("Feature value") 
plt.ylabel("Disease progression") 
plt.title("Simple Linear Regression (y = mx + b)") 
plt.legend()   
plt.show() 
