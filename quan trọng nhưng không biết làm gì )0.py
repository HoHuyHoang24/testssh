from unicodedata import numeric
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
data = np.array([[99,99,99],[99,99,99]])
weight = data[:,0]
height = data[:,1]
age = data[:,2]
regr = linear_model.LinearRegression()
regr.fit(weight.reshape(-1,1),height)
plt.plot(weight,regr.predict(weight.reshape(-1,1)))
need_prediction = int(input(" : "))
for elem in range(need_prediction):
    pass
print(' :',regr.predict([[elem]]))
regr = linear_model.LinearRegression()
regr.fit(weight.reshape(-1,1),age)
plt.plot(weight,regr.predict(weight.reshape(-1,1)))
for elem in range(need_prediction):
    pass
print(' :',regr.predict([[elem]]))
