import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
df=pd.read_csv(r'Квартиры.csv',sep=';')
print(df, df.dtypes)
df['price']=df['price'].str.replace(',','.') 
df['price']=df['price'].astype(float)
plt.scatter(df.area,df.price,color='red')
plt.xlabel('Площадь(кв.м.)')
plt.ylabel('Стоимость(млн.руб)')
plt.show() 
reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
print(reg.predict([[38]]))
print(reg.predict(df[['area']]))
print(reg.coef_)
print(reg.intercept_)
price=reg.coef_ * df.area+reg.intercept_
plt.scatter(df.area,df.price,color='red')
plt.xlabel('Площадь(кв.м.)')
plt.ylabel('Стоимость(млн.руб)')
plt.plot(df.area, reg.predict(df[['area']]))
plt.show()
pred=pd.read_csv(r'Prediction.csv',sep=';')
print(pred)
p=reg.predict([pred['area']].values)
print(p)
pred['price'] = p
print(pred)
pred.to_excel('new.xlsx', index=False)
