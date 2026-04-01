from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20000, 40000, 60000, 80000, 100000])

model = LinearRegression()
model.fit(X, y)


with open('arr_proj_back/models/sal_model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
print("Model trained and saved successfully!")