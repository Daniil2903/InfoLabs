import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, IntSlider
np.random.seed(1)
num_points=50
x_min, x_max=0, 100
y_min, y_max=0, 100
coord=[[np.random.uniform(x_min, x_max), np.random.uniform(y_min, y_max)] for _ in range(num_points)]
x1=[point[0] for point in coord]
y1=[point[1] for point in coord]
k=4
random_points=[
    [np.random.uniform(x_min, x_max), np.random.uniform(y_min, y_max)] for _ in range(k)
]
def kmeans_with_history():
    centers = random_points.copy()
    max_iterations=100
    threshold=0.01
    iteration=0
    history_centers=[centers.copy()]
    history_clusters=[]
    while True:
        iteration+=1
        old_centers=centers.copy()
        clusters=[[] for _ in range(k)]
        for i in range(len(coord)):
            distances=[
                ((centers[j][0]-x1[i])**2+(centers[j][1]-y1[i])** 2)**0.5
                for j in range(k)
            ]
            cluster_index=distances.index(min(distances))
            clusters[cluster_index].append(coord[i])
        history_clusters.append(clusters)
        for j in range(k):
            if clusters[j]: 
                center_x=sum(point[0] for point in clusters[j]) / len(clusters[j])
                center_y=sum(point[1] for point in clusters[j]) / len(clusters[j])
                centers[j]=[center_x, center_y]
        history_centers.append(centers.copy())
        max_shift=max(
            ((old_centers[j][0]-centers[j][0])**2+(old_centers[j][1]-centers[j][1])**2)**0.5
            for j in range(k)
        )
        if max_shift<threshold or iteration>= max_iterations:
            break
    return history_centers, history_clusters, iteration
history_centers, history_clusters, total_iterations=kmeans_with_history()
def visualize_kmeans(iteration):
    centers=history_centers[iteration]
    clusters=history_clusters[iteration]
    plt.figure(figsize=(8,6))
    colors=['red', 'blue', 'green', 'purple']
    for j in range(k):
        if clusters[j]:
            cluster_x=[point[0] for point in clusters[j]]
            cluster_y=[point[1] for point in clusters[j]]
            plt.scatter(cluster_x, cluster_y, color=colors[j], label=f'Кластер {j + 1}')
    center_x=[center[0] for center in centers]
    center_y=[center[1] for center in centers]
    plt.scatter(center_x, center_y, color='black', marker='x', s=100, label='Центры кластеров')
    plt.title(f"Итерация {iteration + 1}")
    plt.legend()
    plt.show()
slider=IntSlider(min=0, max=total_iterations - 1, step=1, value=0, description='Итерация:')
interact(visualize_kmeans, iteration=slider)
