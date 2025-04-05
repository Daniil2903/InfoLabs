import random
import numpy as np
import matplotlib.pyplot as plt
p=0.8
xMin1, xMax1=0, 50
yMin1, yMax1=0, 50
xMin2, xMax2=25, 75
yMin2, yMax2=25, 75
pointsCount1=50
pointsCount2=50
x=[]
y=[]
for _ in range(pointsCount1):
    x.append([random.uniform(xMin1, xMax1), random.uniform(yMin1, yMax1)])
    y.append(0)
for _ in range(pointsCount2):
    x.append([random.uniform(xMin2, xMax2), random.uniform(yMin2, yMax2)])
    y.append(1)
def train_test_split(x, y, p):
    combined=list(zip(x, y))
    random.shuffle(combined)
    split_idx=int(len(combined) * p)
    train=combined[:split_idx]
    test=combined[split_idx:]
    x_train, y_train=zip(*train)
    x_test, y_test=zip(*test)
    return list(x_train), list(x_test), list(y_train), list(y_test)
x_train, x_test, y_train, y_test=train_test_split(x, y, p)
def predict_knn(x_train, y_train, x_test, k):
    y_predict=[]
    for test_point in x_test:
        distances=[np.linalg.norm(np.array(train_point)-np.array(test_point)) for train_point in x_train]
        nearest_indices=np.argsort(distances)[:k]
        nearest_labels=[y_train[i] for i in nearest_indices]
        predicted_label=max(set(nearest_labels), key=nearest_labels.count)
        y_predict.append(predicted_label)
    return y_predict
k=5
y_predict=predict_knn(x_train, y_train, x_test, k)
sovp=sum(1 for true, pred in zip(y_test, y_predict) if true==pred)
accuracy = sovp / len(y_predict)
print(f'Accuracy: {accuracy:.2f}')
def plot_results(x_train, y_train, x_test, y_test, y_predict):
    plt.figure(figsize=(10, 7))
    train_0=[p for p, lbl in zip(x_train, y_train) if lbl==0]
    train_1=[p for p, lbl in zip(x_train, y_train) if lbl==1]
    if train_0:
        plt.scatter(*zip(*train_0), c='blue', marker='o', label='Тренировочный ноль')
    if train_1:
        plt.scatter(*zip(*train_1), c='blue', marker='x', label='Тренировочная единица')
    correct_0=[p for p, t, pred in zip(x_test, y_test, y_predict) if t==pred and t==0]
    correct_1=[p for p, t, pred in zip(x_test, y_test, y_predict) if t==pred and t==1]
    wrong_0=[p for p, t, pred in zip(x_test, y_test, y_predict) if t!=pred and t==0]
    wrong_1=[p for p, t, pred in zip(x_test, y_test, y_predict) if t!=pred and t==1]
    if correct_0:
        plt.scatter(*zip(*correct_0), c='green', marker='o', alpha=0.6, label='Правильный ноль')
    if correct_1:
        plt.scatter(*zip(*correct_1), c='green', marker='x', alpha=0.6, label='Правильная единица')
    if wrong_0:
        plt.scatter(*zip(*wrong_0), c='red', marker='o', alpha=0.6, label='Неправильный ноль')
    if wrong_1:
        plt.scatter(*zip(*wrong_1), c='red', marker='x', alpha=0.6, label='Неправильная единица')
    plt.title(f'Точность = {accuracy:.2f}')
    plt.legend()
    plt.show()
plot_results(x_train, y_train, x_test, y_test, y_predict)
