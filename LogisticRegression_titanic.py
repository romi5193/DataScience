import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

passengers=pd.read_csv('passengers.csv')
passengers.head()

#clean data
passengers['Sex'] = passengers['Sex'].map({'male':0, 'female':1})
mean=passengers['Age'].mean()
passengers.fillna({'Age':mean}, inplace=True)


passengers['FirstClass']= passengers['Pclass'].apply(lambda x: 1 if x== 1 else 0)
passengers['SecondClass']= passengers['Pclass'].apply(lambda x: 1 if x== 2 else 0)

features=passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]
survival=passengers['Survived']

#Split, transform and perform Logistic Regression on dataset
x_train, x_test, y_train, y_test = train_test_split(features, survival, train_size=0.8, test_size=0.2)

normalize=StandardScaler()
normalize.fit_transform(x_train)
normalize.transform(x_test)

log_reg_model=LogisticRegression()
log_reg_model.fit(x_train, y_train)

print('Model Train Score" + str(log_reg_model.score(x_train, y_train)))
print('Model Test Score" + str(log_reg_model.score(x_test, y_test)))

print(list(zip(['Sex','Age','FirstClass','SecondClass'],log_reg_model.coef_[0])))
