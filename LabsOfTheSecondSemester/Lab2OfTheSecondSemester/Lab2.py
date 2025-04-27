##coord=[[0,1],[2,4],[2.34,43], [43,4.3],[34,8], [9,2], [90,89],[67,89]]
##import matplotlib.pyplot as plt
##import numpy as np
##x1=[]
##y1=[]
##for i in range(len(coord)):
##    x1.append(coord[i][0])
##    y1.append(coord[i][1])
##fig, ax=plt.subplots()
##ax.scatter(x1, y1)
##plt.show()
##k=4
##random_points=[[1,3],[3,2],[32,90],[90,14.8]]
##x_min=min(x1)
##x_max=max(x1)
##y_min=min(y1)
##y_max=max(x1)
##dist1=[]
##dist2=[]
##dist3=[]
##dist4=[]
##for i in range(len(coord)):
##    dist1.append(((random_points[0][0]-x1[i])**2+(random_points[0][1]-y1[i])**2)**0.5)
##    dist2.append(((random_points[1][0]-x1[i])**2+(random_points[1][1]-y1[i])**2)**0.5)
##    dist3.append(((random_points[2][0]-x1[i])**2+(random_points[2][1]-y1[i])**2)**0.5)
##    dist4.append(((random_points[3][0]-x1[i])**2+(random_points[3][1]-y1[i])**2)**0.5)
##claster=[]
##for i in range(len(coord)):
##    if dist1[i]< dist2[i] and dist1[i]< dist3[i] and dist1[i]< dist4[i]:
##        claster.append(1)
##    elif dist2[i]< dist2[i] and dist2[i]< dist3[i] and dist2[i]< dist4[i]:
##        claster.append(2)
##    elif dist3[i]< dist1[i] and dist3[i]< dist2[i] and dist3[i]< dist4[i]:
##        claster.append(3)
##    elif dist4[i]< dist1[i] and dist4[i]< dist2[i] and dist4[i]< dist3[i]:
##        claster.append(4)
##
##
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from ipywidgets import interact

# Генерация данных
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=42)

# Функция для отображения кластеризации на заданной итерации
def plot_kmeans_iteration(iteration):
    # Создаем объект KMeans с ограничением на количество итераций
    kmeans = KMeans(n_clusters=3, max_iter=iteration, n_init=1, random_state=42)
    kmeans.fit(X)
    
    # Получаем метки кластеров и центроиды
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Отрисовываем точки и центроиды
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis', label='Точки данных')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, label='Центроиды')
    plt.title(f"Итерация {iteration}")
    plt.legend()
    plt.show()

# Создаем интерактивный ползунок для выбора итерации
interact(plot_kmeans_iteration, iteration=(1, 10, 1))
