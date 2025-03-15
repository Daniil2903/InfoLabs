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
    y.append(1)
for j in range(pointsCount2):
    x.append([random.uniform(xMin2,xMax2),random.uniform(yMin2,yMax2)])
    y.append(2)
print(x)     
print(y)  
def train_test_split(x,y,p):
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for i in range(round((pointsCount1 + pointsCount2)*p)):
        x_train.append(x[i])
        y_train.append(y[i])
    for l in range(round((pointsCount1 + pointsCount2)*(1-p))):
        x_test.append(x[l])
        y_test.append(y[l])
        
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
    if y_predict1[i]==y_test[i]:
        sovp+=1
accuracy=sovp/len(y_predict1)
print(accuracy)







