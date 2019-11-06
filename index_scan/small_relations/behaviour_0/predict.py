import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

loaded_model = pickle.load(open('/home/dsladmin/Documents/vishal/index_scan/vu_model_0/model.sav', 'rb'))

temp = np.loadtxt('/home/dsladmin/Documents/vishal/index_scan/vu_model_0/test_data.txt')

X = []

for i in range(temp.size):
	X.append([])
	X[i].append(temp[i]**0.5)
	X[i].append(temp[i])
	X[i].append(temp[i]**2)

np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vu_model_0/predictions.txt',loaded_model.predict(X))

# result = loaded_model.score(X_test, Y_test)
# print(result)