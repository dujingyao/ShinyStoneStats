import pandas as pd

df = pd.read_csv('diamonds_数据集.csv')
data = df
# 读取文档的行数和列数
# print(data.shape)
# 数据类型
# print(df.info())
# 基本信息统计
# print(data.describe())
# 返回所有列名
# print(data.columns)
# 查看某一列唯一值
# print(data['color'].unique())
# 数据清洗
# 判断各变量中是否存在缺失值
# print(data.isnull().any(axis=0))
# 判断数据行中是否存在缺失值
# print(data.isnull().any(axis=1))
# 定位缺失值所在的行
# print(data.loc[data.isnull().any(axis=1)])
# 各变量中缺失值的数量
print()

