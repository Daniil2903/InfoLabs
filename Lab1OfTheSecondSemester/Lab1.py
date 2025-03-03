import random
xMin1=0
xMax1=50
yMin1=0
yMax1=50
xMin2=25
xMax2=75
yMin2=25
yMax2=75
k=3
classCount=2
pointCount1=50
pointCount2=50
x=[]
y=[]
for i in range(pointCount1):
    x.append([random.uniform(xMin1, xMax1), random.uniform(yMin1, yMax1)])
for i in range(pointCount2):
    x.append([random.uniform(xMin2, xMax2), random.uniform(yMin2, yMax2)])
for i in range(pointCount1):
    y.append(1)
for i in range(pointCount2):
    y.append(0)
p=0.8
def TrainAndTest(x, y, p):
    x_train=[]
    y_train=[]
    x_test=[]
    y_test=[]
    for i in range(round((pointCount1+pointCount2)*p)):
        x_train.append(x[i])
        y_train.append(y[i])
    for i in range(round((pointCount1+pointCount2)*(1-p))):
        x_test.append(x[i])
        y_test.append(y[i])
    return(x_train, y_train, x_test,  y_test)
print(TrainAndTest(x, y, p))
