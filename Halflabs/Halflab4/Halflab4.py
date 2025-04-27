import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
df = pd.read_csv(r'Квартиры.csv', sep=';')
print(df, df.dtypes)
df['price'] = df['price'].str.replace(',', '.', regex=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df.dropna(subset=['area', 'price'], inplace=True)
plt.scatter(df.area, df.price, color='red')
plt.xlabel('Площадь(кв.м.)')
plt.ylabel('Стоимость(млн.руб)')
plt.show()
reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)
print("Предсказанная стоимость для площади 38 кв.м:", reg.predict([[38]]))
predictions = reg.predict(df[['area']])
print("Предсказания:", predictions)
print("Коэффициент:", reg.coef_)
print("Свободный член:", reg.intercept_)
plt.scatter(df.area, df.price, color='red')
plt.plot(df.area, predictions, color='blue')
plt.xlabel('Площадь(кв.м.)')
plt.ylabel('Стоимость(млн.руб)')
plt.show()
pred = pd.read_csv(r'Prediction.csv', sep=';')
print(pred)
p = reg.predict(pred[['area']])
pred['price'] = p.flatten()  # Преобразуем в одномерный массив
print(pred)
pred.to_excel('Prediction.xlsx', index=False)

