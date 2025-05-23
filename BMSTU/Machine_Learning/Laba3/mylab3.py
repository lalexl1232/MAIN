# -*- coding: utf-8 -*-
"""Mylab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QakghhcT9Lrmq08sbodJ9v9RwlSQZip2
"""

import numpy as np
import seaborn as sns
import pandas as pd
from google.colab import files

file = files.upload()

df = pd.read_csv('heart.csv')
ds = df.copy()
df.head(15)

ds.shape

ds.describe()

from sklearn.preprocessing import LabelEncoder
lbl = LabelEncoder()
ds['Sex'] = lbl.fit_transform(ds['Sex'])
ds['ExerciseAngina'] = lbl.fit_transform(ds['ExerciseAngina'])

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
transformed = ohe.fit_transform(ds[['ChestPainType']])
ds[ohe.categories_[0]] = transformed.toarray()
ds.drop('ChestPainType', axis = 1, inplace = True)

transformed = ohe.fit_transform(ds[['RestingECG']])
ds[ohe.categories_[0]] = transformed.toarray()
ds.drop('RestingECG', axis = 1, inplace = True)

transformed = ohe.fit_transform(ds[['ST_Slope']])
ds[ohe.categories_[0]] = transformed.toarray()
ds.drop('ST_Slope', axis = 1, inplace = True)

ds.head(10)

from sklearn.model_selection import train_test_split
y = ds['HeartDisease']
x = ds.drop(columns = 'HeartDisease')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 13)
x_test.shape

from sklearn.linear_model import SGDClassifier
model1 = SGDClassifier(penalty='l1', alpha= 0.001, random_state= 7, 
                       n_iter_no_change=100, class_weight= 'balanced', average= 1)
model1.fit(x_train, y_train)

"""loss='hinge', *, penalty='l2', alpha=0.0001, l1_ratio=0.15, fit_intercept=True, max_iter=1000, tol=0.001, shuffle=True, verbose=0, epsilon=0.1, n_jobs=None, random_state=None, learning_rate='optimal', eta0=0.0, power_t=0.5, early_stopping=False, validation_fraction=0.1, n_iter_no_change=5, class_weight=None, warm_start=False, average=False"""

from sklearn.metrics import accuracy_score
accuracy_score(y_test, model1.predict(x_test))

from sklearn.metrics import recall_score
recall_score(y_test, model1.predict(x_test))

from sklearn.metrics import f1_score
f1_score(y_test, model1.predict(x_test))

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
cm = confusion_matrix(y_test, model1.predict(x_test))
plt.figure(figsize=(10,8))
sns.heatmap(cm, annot=True)

from sklearn.linear_model import LogisticRegression
model2 = LogisticRegression(class_weight= 'balanced', max_iter= 100)
model2.fit(x_train, y_train)

"""penalty='l2', *, dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, multi_class='auto', verbose=0, warm_start=False, n_jobs=None, l1_ratio=None"""

accuracy_score(y_test, model2.predict(x_test))

recall_score(y_test, model2.predict(x_test))

f1_score(y_test, model2.predict(x_test))

cm = confusion_matrix(y_test, model2.predict(x_test))
plt.figure(figsize=(10,8))
sns.heatmap(cm, annot=True)

"""**модель на данных стандартизированных StandartScaler**"""

from sklearn.preprocessing import StandardScaler
ds2 = ds.copy()
scaler = StandardScaler()
ds2[['RestingBP']] = scaler.fit_transform(ds2[['RestingBP']])
ds2[['Cholesterol']] = scaler.fit_transform(ds2[['Cholesterol']])
ds2[['MaxHR']] = scaler.fit_transform(ds2[['MaxHR']])
ds2.head()

ds2.describe()

from sklearn.model_selection import train_test_split
y = ds2['HeartDisease']
x = ds2.drop(columns = 'HeartDisease')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 13)
x_test.shape

from sklearn.linear_model import SGDClassifier
model1 = SGDClassifier(loss='hinge', penalty='l1', alpha= 0.001, random_state= 7, 
                       n_iter_no_change=100, class_weight= 'balanced', average= 1)
model1.fit(x_train, y_train)

"""loss='hinge', *, penalty='l2', alpha=0.0001, l1_ratio=0.15, fit_intercept=True, max_iter=1000, tol=0.001, shuffle=True, verbose=0, epsilon=0.1, n_jobs=None, random_state=None, learning_rate='optimal', eta0=0.0, power_t=0.5, early_stopping=False, validation_fraction=0.1, n_iter_no_change=5, class_weight=None, warm_start=False, average=False"""

from sklearn.metrics import accuracy_score
accuracy_score(y_test, model1.predict(x_test))

from sklearn.metrics import recall_score
recall_score(y_test, model1.predict(x_test))

from sklearn.metrics import f1_score
f1_score(y_test, model1.predict(x_test))

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
cm = confusion_matrix(y_test, model1.predict(x_test))
plt.figure(figsize=(10,8))
sns.heatmap(cm, annot=True)

from sklearn.linear_model import LogisticRegression
model2 = LogisticRegression(class_weight= 'balanced', tol = 1, max_iter= 1000)
model2.fit(x_train, y_train)

"""penalty='l2', *, dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, multi_class='auto', verbose=0, warm_start=False, n_jobs=None, l1_ratio=None"""

accuracy_score(y_test, model2.predict(x_test))

recall_score(y_test, model2.predict(x_test))

f1_score(y_test, model2.predict(x_test))

cm = confusion_matrix(y_test, model2.predict(x_test))
plt.figure(figsize=(10,8))
sns.heatmap(cm, annot=True)

"""**модель на данных стандартизированных MinMaxScaler**"""

from sklearn.preprocessing import MinMaxScaler
ds3 = ds.copy()
scaler = MinMaxScaler()
ds3[['RestingBP']] = scaler.fit_transform(ds[['RestingBP']])
ds3[['Cholesterol']] = scaler.fit_transform(ds[['Cholesterol']])
ds3[['MaxHR']] = scaler.fit_transform(ds[['MaxHR']])
ds3.head()

ds3.describe()

from sklearn.model_selection import train_test_split
y = ds3['HeartDisease']
x = ds3.drop(columns = 'HeartDisease')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 13)
x_test.shape

from sklearn.linear_model import SGDClassifier
model1 = SGDClassifier(loss='hinge', penalty='l1', alpha= 0.001, random_state= 7, 
                       n_iter_no_change=100, class_weight= 'balanced', average= 1)
model1.fit(x_train, y_train)

"""loss='hinge', *, penalty='l2', alpha=0.0001, l1_ratio=0.15, fit_intercept=True, max_iter=1000, tol=0.001, shuffle=True, verbose=0, epsilon=0.1, n_jobs=None, random_state=None, learning_rate='optimal', eta0=0.0, power_t=0.5, early_stopping=False, validation_fraction=0.1, n_iter_no_change=5, class_weight=None, warm_start=False, average=False"""

from sklearn.metrics import accuracy_score
accuracy_score(y_test, model1.predict(x_test))

from sklearn.metrics import recall_score
recall_score(y_test, model1.predict(x_test))

from sklearn.metrics import f1_score
f1_score(y_test, model1.predict(x_test))

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
cm = confusion_matrix(y_test, model1.predict(x_test))
plt.figure(figsize=(10,8))
sns.heatmap(cm, annot=True)

from sklearn.linear_model import LogisticRegression
model2 = LogisticRegression(class_weight= 'balanced', tol = 1, max_iter= 1000)
model2.fit(x_train, y_train)

"""penalty='l2', *, dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, multi_class='auto', verbose=0, warm_start=False, n_jobs=None, l1_ratio=None"""

accuracy_score(y_test, model2.predict(x_test))

recall_score(y_test, model2.predict(x_test))

f1_score(y_test, model2.predict(x_test))

cm = confusion_matrix(y_test, model2.predict(x_test))
plt.figure(figsize=(10,8))
sns.heatmap(cm, annot=True)