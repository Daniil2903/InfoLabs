import random as dandy
dandy.seed(1)
x1=dandy.randint(0, 11)
x2=dandy.randint(0, 11)
x3=dandy.randint(0, 11)
print(x1, x2, x3)
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_blobs, make_moons, make_circles
from sklearn.cluster import MiniBatchKMeans, AffinityPropagation, OPTICS
from sklearn.svm import SVC
from sklearn.metrics import adjusted_rand_score
from matplotlib.colors import ListedColormap
def generate_data(data_type='blobs', n_samples=500, noise=0.05):
    if data_type == 'blobs':
        X, y = make_blobs(n_samples=n_samples, centers=2, cluster_std=1.2, random_state=42)
    elif data_type == 'moons':
        X, y = make_moons(n_samples=n_samples, noise=noise)
    elif data_type == 'circles':
        X, y = make_circles(n_samples=n_samples, factor=0.5, noise=noise)
    elif data_type == 'random':
        X, y = make_blobs(n_samples=n_samples, centers=2, cluster_std=3.0, random_state=42)
    elif data_type == 'density':
        X1 = np.random.normal(loc=0, scale=0.3, size=(200, 2))
        X2 = np.random.normal(loc=3, scale=1.0, size=(300, 2))
        X = np.vstack((X1, X2))
        y = np.hstack((np.zeros(200), np.ones(300)))
    elif data_type == 'noisy':
        X, y = make_blobs(n_samples=n_samples, centers=2, cluster_std=2.5, random_state=42)
        X = np.vstack([X, np.random.uniform(low=-10, high=10, size=(50, 2))])
        y = np.hstack([y, np.full(50, -1)])
    else:
        raise ValueError("Unknown data type")
    return X, y
def plot_clusters(X, y_true, labels, method_name, ari, ax):
    cmap = ListedColormap(['#377eb8', '#ff7f00', '#4daf4a'])
    ax.scatter(X[:, 0], X[:, 1], c=labels, cmap=cmap, s=30, edgecolor='k')
    if len(np.unique(labels)) == 2:
        try:
            svm = SVC(kernel='linear', C=1000)
            svm.fit(X, labels)
            x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
            y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
            xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                                 np.arange(y_min, y_max, 0.02))
            Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            ax.contourf(xx, yy, Z, alpha=0.2, cmap=cmap)
            ax.contour(xx, yy, Z, colors='beige', linewidths=2, 
                      linestyles='dashed', levels=[0])
        except:
            pass
    ax.set_title(f"{method_name}\nARI: {ari:.2f}", fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
data_types = ['blobs', 'moons', 'circles', 'random', 'density', 'noisy']
methods = {
    'MiniBatch KMeans': MiniBatchKMeans(n_clusters=2, random_state=42),
    'Affinity Propagation': AffinityPropagation(damping=0.75, preference=-30),
    'OPTICS': OPTICS(min_samples=20, xi=0.05)
}
results = []
plt.figure(figsize=(15, 20))
for idx, data_type in enumerate(data_types):
    X, y_true = generate_data(data_type)
    for col, (method_name, model) in enumerate(methods.items()):
        ax = plt.subplot(len(data_types), len(methods), idx*len(methods) + col + 1)
        try:
            labels = model.fit_predict(X)
            if method_name == 'OPTICS':
                labels[labels == -1] = max(labels) + 1
            ari = adjusted_rand_score(y_true, labels)
            results.append([data_type, method_name, ari])
            plot_clusters(X, y_true, labels, method_name, ari, ax)
        except Exception as e:
            print(f"Ошибка {method_name} на {data_type}: {str(e)}")
            ax.set_title(f"{method_name}\nError", color='red')
            ax.set_axis_off()
plt.tight_layout()
plt.subplots_adjust(top=0.95)
plt.show()
df = pd.DataFrame(results, columns=['Data', 'Method', 'ARI'])
pivot_df = df.pivot(index='Data', columns='Method', values='ARI').round(2)
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
table = ax.table(
    cellText=pivot_df.values,
    rowLabels=pivot_df.index,
    colLabels=pivot_df.columns,
    cellLoc='center',
    loc='center',
    colColours=['#f0f0f0']*3,
    rowColours=['#f0f0f0']*6
)
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 1.5)
for i in range(len(pivot_df.index)):
    for j in range(len(pivot_df.columns)):
        table[(i+1, j)].set_facecolor(plt.cm.Blues(pivot_df.iloc[i,j]))
plt.title("Результаты кластеризации\nAdjusted Rand Index", pad=20)
plt.show()
