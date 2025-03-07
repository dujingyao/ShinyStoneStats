import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import pandas as pd
import matplotlib.font_manager as fm
from adjustText import adjust_text

# 确保matplotlib能够显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体或者你系统中存在的其他中文字体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号'-'显示为方块的问题

# 示例文本数据
texts = ["数字化", "技术装备", "智能化", "农产品", "因地制宜",
         "信息化", "机器人", "推广应用", "贯彻落实", "信息技术",
         "现代化", "核心技术", "互联网", "建立健全", "规模化"]

# 创建TF-IDF向量化器
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 4))
X_sparse = vectorizer.fit_transform(texts)

# 将稀疏矩阵转换为稠密矩阵
X_dense = X_sparse.toarray()

# 定义聚类数量k
k = 4

# 初始化层次聚类模型
clustering = AgglomerativeClustering(n_clusters=k, linkage='ward')

# 拟合模型
labels = clustering.fit_predict(X_dense)

# 将文本和标签组合，并按簇分组
clusters = defaultdict(list)
for text, label in zip(texts, labels):
    clusters[label].append(text)

# 输出每个簇的内容
for cluster_id, words in clusters.items():
    print(f"簇 {cluster_id}:")
    for word in words:
        print(f"  - {word}")
    print()

# 使用PCA降维到2D以进行可视化
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(X_dense)

# 绘制散点图
plt.figure(figsize=(12, 8))  # 增大图表尺寸
scatter = sns.scatterplot(x=reduced_features[:, 0], y=reduced_features[:, 1], hue=labels, palette='viridis', s=100)

# 添加标签并调整位置以避免重叠
texts_for_adjustment = []
for i, text in enumerate(texts):
    texts_for_adjustment.append(plt.text(reduced_features[i, 0], reduced_features[i, 1], text, fontsize=9, ha='center', va='center'))

# 调整标签位置
adjust_text(texts_for_adjustment, arrowprops=dict(arrowstyle='->', color='gray'))

plt.title("层次聚类可视化使用PCA（杜净瑶2307385106)")
plt.xlabel("主成分1")
plt.ylabel("主成分2")
plt.savefig('可视化图.png')
# plt.close()
# # plt.show()