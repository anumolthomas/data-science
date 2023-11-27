import numpy as np
import pandas as pd
student=pd.read_csv('student_score.csv')
print(student.head())
student.describe()
student.info()
import matplotlib.pyplot as plt
Xax=student.iloc[:,0]
Yax=student.iloc[:,1]
plt.scatter(Xax,Yax)
plt.xlabel("no of hours:")
plt.ylabel("score:")
plt.title("student scores:")
plt.show()
X=student.iloc[:,:-1]
Y=student.iloc[:,1]
print('X values:')
print(X)
print('Y values:')
print(Y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
print(X_train)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
print('INTERCEPT=',regressor.intercept_)
print('CO-EFFICENT=',regressor.coef_)
y_pred=regressor.predict(X_test)
for(i,j) in zip(y_test,y_pred):
    if(i!=j):
        print("Actual value:",i,"predicted value:",j)
print("number of mislabeled points from test data set:",(y_test!=y_pred).sum())
from sklearn import metrics
print("Mean Absolute error :", metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared error :", metrics.mean_squared_error(y_test,y_pred))
print("Root Mean Squared error :", np.sqrt(metrics.mean_squared_error(y_test,y_pred)))