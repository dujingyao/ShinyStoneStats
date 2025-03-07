import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

# 加载数据
file_path = 'diamonds_预处理后.csv'
data = pd.read_csv(file_path)

# 查看数据前几行
print(data.head())

# 查看数据的基本信息
print(data.info())

# 检查缺失值
print(data.isnull().sum())
# 分类变量的分布（条形图）


# 设置绘图风格
sns.set(style="whitegrid")

# 创建子图
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# 绘制切割质量(cut) 的分布
sns.countplot(x='cut', data=data, ax=axes[0])
axes[0].set_title("切割质量(cut)的分布", fontproperties='SimHei')

# 绘制 color 的分布
sns.countplot(x='color', data=data, ax=axes[1])
axes[1].set_title('颜色(color)的分布', fontproperties='SimHei')

# 绘制 clarity 的分布
sns.countplot(x='clarity', data=data, ax=axes[2])
axes[2].set_title('钻石净度(clarity)的分布', fontproperties='SimHei')

plt.tight_layout()
plt.savefig('分类变量的分布.png')
plt.show()

# 数值变量的分布（直方图和箱线图）
# 创建子图
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 绘制 carat 的分布
sns.histplot(data['carat'], bins=30, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('克拉重量(carat)的分布', fontproperties='SimHei')

# 绘制 depth 的分布
sns.boxplot(data['depth'], ax=axes[0, 1])
axes[0, 1].set_title('深度百分比(depth)的分布', fontproperties='SimHei')

# 绘制 table 的分布
sns.histplot(data['table'], bins=30, kde=True, ax=axes[1, 0])
axes[1, 0].set_title('桌面宽度百分比(table)的分布', fontproperties='SimHei')

# 绘制 price 的分布
sns.histplot(data['price'], bins=30, kde=True, ax=axes[1, 1])
axes[1, 1].set_title('价格(Price)的分布', fontproperties='SimHei')

plt.tight_layout()
plt.savefig('数值变量的分布.png')
plt.show()


# 相关性矩阵（热力图）
# 计算数值变量的相关性矩阵
corr_matrix = data[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].corr()

# 绘制热力图
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title("数值特征的相关矩阵", fontproperties='SimHei')
plt.savefig("相关性矩阵.png")
plt.show()

# 价格与其他特征的关系（散点图）
# 创建子图
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 绘制 carat 和 price 的关系
sns.scatterplot(x='carat', y='price', data=data, ax=axes[0, 0])
axes[0, 0].set_title('克拉 VS 价格', fontproperties='SimHei')

# 绘制 depth 和 price 的关系
sns.scatterplot(x='depth', y='price', data=data, ax=axes[0, 1])
axes[0, 1].set_title('深度 VS 价格', fontproperties='SimHei')

# 绘制 table 和 price 的关系
sns.scatterplot(x='table', y='price', data=data, ax=axes[0, 2])
axes[0, 2].set_title('桌面宽度百分比 vs 价格', fontproperties='SimHei')

# 绘制 x 和 price 的关系
sns.scatterplot(x='x', y='price', data=data, ax=axes[1, 0])
axes[1, 0].set_title('X vs 价格', fontproperties='SimHei')

# 绘制 y 和 price 的关系
sns.scatterplot(x='y', y='price', data=data, ax=axes[1, 1])
axes[1, 1].set_title('Y vs 价格', fontproperties='SimHei')

# 绘制 z 和 price 的关系
sns.scatterplot(x='z', y='price', data=data, ax=axes[1, 2])
axes[1, 2].set_title('Z vs 价格', fontproperties='SimHei')

plt.tight_layout()
plt.savefig('价格与其他特征的关系.png')
plt.show()

# 分类变量对价格的影响（箱线图）
# 创建子图
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# 绘制 cut 对 price 的影响

sns.boxplot(x='cut', y='price', data=data, ax=axes[0])
axes[0].set_title('切割质量 vs 价格', fontproperties='SimHei')

# 绘制 color 对 price 的影响
sns.boxplot(x='color', y='price', data=data, ax=axes[1])
axes[1].set_title('颜色 vs 价格', fontproperties='SimHei')

# 绘制 clarity 对 price 的影响
sns.boxplot(x='clarity', y='price', data=data, ax=axes[2])
axes[2].set_title('净度 vs 价格', fontproperties='SimHei')

plt.tight_layout()
plt.savefig('分类变量对价格的影响.png')
plt.show()
