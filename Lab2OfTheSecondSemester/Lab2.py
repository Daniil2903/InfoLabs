import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
np.random.seed(1)
num_points=50
x_min, x_max=0, 100
y_min, y_max=0, 100
coord = [[np.random.uniform(x_min, x_max), np.random.uniform(y_min, y_max)] for _ in range(num_points)]
x1=[point[0] for point in coord]
y1=[point[1] for point in coord]
k=4
random_points=[
    [np.random.uniform(x_min, x_max), np.random.uniform(y_min, y_max)] for _ in range(k)
]
def kmeans_with_history():
    centers=random_points.copy()
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
                ((centers[j][0] - x1[i])**2 + (centers[j][1] - y1[i])**2)**0.5
                for j in range(k)
            ]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(coord[i])
        history_clusters.append(clusters)
        for j in range(k):
            if clusters[j]:
                center_x = sum(point[0] for point in clusters[j]) / len(clusters[j])
                center_y = sum(point[1] for point in clusters[j]) / len(clusters[j])
                centers[j] = [center_x, center_y]
        history_centers.append(centers.copy())
        max_shift = max(
            ((old_centers[j][0] - centers[j][0])**2 + (old_centers[j][1] - centers[j][1])**2)**0.5
            for j in range(k)
        )
        if max_shift < threshold or iteration >= max_iterations:
            break
    return history_centers, history_clusters, iteration
history_centers, history_clusters, total_iterations = kmeans_with_history()
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.2)
colors = ['red', 'blue', 'green', 'purple']
iteration = 0
centers = history_centers[iteration]
clusters = history_clusters[iteration]
scatter_plots = []
for j in range(k):
    if clusters[j]: 
        cluster_x = [point[0] for point in clusters[j]]
        cluster_y = [point[1] for point in clusters[j]]
        scatter = ax.scatter(cluster_x, cluster_y, color=colors[j], label=f'Кластер {j + 1}')
        scatter_plots.append(scatter)
center_x = [center[0] for center in centers]
center_y = [center[1] for center in centers]
centers_plot = ax.scatter(center_x, center_y, color='black', marker='x', s=100, label='Центры кластеров')
ax.set_title(f"Итерация {iteration + 1}")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
ax.grid(True)
ax_slider = plt.axes([0.2, 0.05, 0.65, 0.03]) 
slider = Slider(ax_slider, 'Итерация', 0, total_iterations - 1, valinit=0, valstep=1)
def update(val):
    iteration = int(slider.val)
    centers = history_centers[iteration]
    clusters = history_clusters[iteration]
    for j in range(k):
        if clusters[j]: 
            cluster_x = [point[0] for point in clusters[j]]
            cluster_y = [point[1] for point in clusters[j]]
            scatter_plots[j].set_offsets(np.c_[cluster_x, cluster_y])
        else:
            scatter_plots[j].set_offsets([]) 
    center_x = [center[0] for center in centers]
    center_y = [center[1] for center in centers]
    centers_plot.set_offsets(np.c_[center_x, center_y])
    ax.set_title(f"Итерация {iteration + 1}")
    fig.canvas.draw_idle()
slider.on_changed(update)
plt.show()
