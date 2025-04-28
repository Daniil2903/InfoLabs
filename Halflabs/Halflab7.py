import time
import warnings
from itertools import cycle, islice

import matplotlib.pyplot as plt
import numpy as np
import math
import random

# Кластеризаторы
from sklearn import cluster, datasets, mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler

# Классификаторы
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neural_network import MLPClassifier

# Регрессии
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import BayesianRidge
from sklearn.kernel_ridge import KernelRidge
from sklearn.svm import SVR
from sklearn.svm import NuSVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
n_samples = 500
seed = 30

noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed)

x, y = noisy_circles

colors = ['y', 'g']

fig, ax = plt.subplots()
                                                                                                                                                                                                  
for i in range(len(x)):
    ax.scatter(x[[i], 0], x[[i], 1], c=colors[y[i]])
plt.show()
temp_x = np.linspace(x[:, 0].min() - 1, x[:, 0].max() + 1, 100)
temp_y = np.linspace(x[:, 1].min() - 1, x[:, 1].max() + 1, 100)

print(temp_x.shape)
print(temp_y.shape)
print(temp_x[:5])
print(temp_y[:5])

temp_x = np.linspace(x[:, 0].min() - 1, x[:, 0].max() + 1, 100)
temp_y = np.linspace(x[:, 1].min() - 1, x[:, 1].max() + 1, 100)

print(temp_x.shape)
print(temp_y.shape)
print(temp_x[:5])
print(temp_y[:5])
xx, yy = np.meshgrid(temp_x, temp_y)

print(xx.shape)
print(yy.shape)
print(xx[:5, :5])
print(yy[:5, :5])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

x_train = np.asarray(x_train)
x_test = np.asarray(x_test)
y_train = np.asarray(y_train)
y_test = np.asarray(y_test)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x_train, y_train)
y_pred = neigh.predict(x_test)

# Предсказание для сетки
Z = neigh.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
accuracy = accuracy_score(y_test, y_pred)
print('accuracy: ', accuracy)

print('Матрица ошибок:')
print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

markers = ['x', 'o']

fig, ax = plt.subplots()
plt.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')  # Области классов

for i in range(len(x_train)):
    ax.scatter(x_train[i, 0], x_train[i, 1], marker=markers[y_train[i]], c='b')

for i in range(len(x_test)):
    m = 'r'
    if y_test[i] == y_pred[i]:
        m = 'g'
    ax.scatter(x_test[i, 0], x_test[i, 1], marker=markers[y_test[i]], c=m)
plt.show()

