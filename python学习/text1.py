import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def visualize_clusters(X, labels, num_clusters, method='pca', savefig=False):
    # 将稀疏矩阵转换为稠密矩阵（如果 X 是稀疏矩阵）
    if hasattr(X, 'toarray'):
        X_dense = X.toarray()
    else:
        X_dense = X

    if method == 'pca':
        # 使用 PCA 进行降维，将特征向量从高维空间转换到二维空间以便于可视化
        reducer = PCA(n_components=2)
    elif method == 'tsne':
        # 使用 t-SNE 进行降维，将特征向量从高维空间转换到二维空间以便于可视化
        reducer = TSNE(n_components=2, random_state=0)
    else:
        raise ValueError("Invalid method. Choose 'pca' or 'tsne'.")

    X_reduced = reducer.fit_transform(X_dense)

    # 绘制散点图
    plt.figure(figsize=(10, 8))
    for i in range(num_clusters):
        cluster_points = [X_reduced[j] for j in range(len(labels)) if labels[j] == i]
        cluster_points = np.array(cluster_points)
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i}')

    plt.title('K-Means Clustering of Keywords')
    if method == 'pca':
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
    elif method == 'tsne':
        plt.xlabel('t-SNE Dimension 1')
        plt.ylabel('t-SNE Dimension 2')
    plt.legend()

    if savefig:
        plt.savefig('可视化图.png')

    plt.show()

# 示例调用
# 假设你已经有了 X 和 labels
# visualize_clusters(X, labels, num_clusters=4, method='pca', savefig=True)