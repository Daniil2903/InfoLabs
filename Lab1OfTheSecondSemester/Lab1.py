import random
import heapq
p = 0.8
xMin1 = 0
xMax1 = 50
yMin1 = 0
yMax1 = 50
xMin2 = 25
xMax2 = 75
yMin2 = 25
yMax2 = 75
k = 3
classesCount = 2
pointsCount1 = 50
pointsCount2 = 50
x = []
y = []
for i in range(pointsCount1):
    x.append([random.uniform(xMin1,xMax1),random.uniform(yMin1,yMax1)])
    y.append(0)
for j in range(pointsCount2):
    x.append([random.uniform(xMin2,xMax2),random.uniform(yMin2,yMax2)])
    y.append(1)
print(x)     
print(y)  
def train_test_split(x,y,p):
    combined=list(zip(x, y))
    random.shuffle(combined)
    split_idx=int(len(combined)*p)
    train=combined[:split_idx]
    test=combined[split_idx:]
    x_train, y_train=zip(*train)
    x_test, y_test=zip(*test)
    
    return x_train, x_test, y_train, y_test
x_train, x_test, y_train, y_test = train_test_split(x,y,p)                                                                                                        
def Pred(x_train, y_train, x_test):
    k=3
    r=[]
    indi=[]
    o12=0
    x12=0
    y_predict=[]
    for i in range(len(x_test)):
        r=[]
        for j in range(len(x_train)):
            r.append((((x_train[j][0]-x_test[i][0])**2)+(x_train[j][1]-x_test[i][1])**2)**0.5)
        a=heapq.nsmallest(k, r)
        indi=[]
        for i in range(len(a)):
            indi.append(r.index(a[i]))
            if y_train[indi[i]]==1:
                o12+=1
            else:
                x12+=1
        if o12>x12:
            y_predict.append(1)
        else:
            y_predict.append(2)
        print(indi)
    return y_predict
y_predict1=Pred(x_train, y_train, x_test)
sovp=0
for i in range(len(y_predict1)):
    if y_test[i]==y_predict1[i]:
        sovp+=1
accuracy=sovp/len(y_predict1)
print('Accuracy:', accuracy)
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
train_0=[p for p, lbl in zip(x_train, y_train) if lbl==0]
def plot_results(x_train, y_train, x_test, y_test, y_predict1):
    plt.figure(figsize=(10, 7))
    train_0 = [p for p, lbl in zip(x_train, y_train) if lbl == 0]
    train_1 = [p for p, lbl in zip(x_train, y_train) if lbl == 1]
    if train_0:
        plt.scatter(*zip(*train_0), c='blue', marker='o', label='Тренировочный ноль')
    if train_1:
        plt.scatter(*zip(*train_1), c='blue', marker='x', label='Тренировочная единица')
    correct_0 = []
    correct_1 = []
    wrong_0 = []
    wrong_1 = []
    for i in range(len(x_test)):
        point = x_test[i]
        true_lbl = y_test[i]
        pred_lbl = y_predict1[i]
        if true_lbl == pred_lbl:
            if true_lbl == 0:
                correct_0.append(point)
            else:
                correct_1.append(point)
        else:
            if true_lbl == 0:
                wrong_0.append(point)
            else:
                wrong_1.append(point)
    if correct_0:
        plt.scatter(*zip(*correct_0), c='green', marker='o', alpha=0.6, label='Правильный ноль')
    if correct_1:
        plt.scatter(*zip(*correct_1), c='green', marker='x', alpha=0.6, label='Правильная единица')
    if wrong_0:
        plt.scatter(*zip(*wrong_0), c='red', marker='o', alpha=0.6, label='Неправильный ноль')
    if wrong_1:
        plt.scatter(*zip(*wrong_1), c='red', marker='x', alpha=0.6, label='Неправильная единица')
    plt.title(f'Точность={accuracy:.2f}')
    plt.legend()
    plt.show()
plot_results(x_train, y_train, x_test, y_test, y_predict1)





