import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Загрузка данных
df = pd.read_csv(r'Квартиры.csv', sep=';')
print(df, df.dtypes)

# Преобразование price в числовой формат
df['price'] = df['price'].str.replace(',', '.', regex=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Удаление строк с пропущенными значениями
df.dropna(subset=['area', 'price'], inplace=True)

# Визуализация данных
plt.scatter(df.area, df.price, color='red')
plt.xlabel('Площадь(кв.м.)')
plt.ylabel('Стоимость(млн.руб)')
plt.show()

# Линейная регрессия
reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)

# Предсказание для одной квартиры
print("Предсказанная стоимость для площади 38 кв.м:", reg.predict([[38]]))

# Предсказание для всех данных
predictions = reg.predict(df[['area']])
print("Предсказания:", predictions)
print("Коэффициент:", reg.coef_)
print("Свободный член:", reg.intercept_)

# График с линией регрессии
plt.scatter(df.area, df.price, color='red')
plt.plot(df.area, predictions, color='blue')
plt.xlabel('Площадь(кв.м.)')
plt.ylabel('Стоимость(млн.руб)')
plt.show()

# Загрузка данных для предсказания
pred = pd.read_csv(r'Prediction.csv', sep=';')
print(pred)

# Предсказание стоимости для новых данных
p = reg.predict(pred[['area']])
pred['price'] = p.flatten()  # Преобразуем в одномерный массив
print(pred)

# Экспорт в Excel
pred.to_excel('Prediction.xlsx', index=False)

