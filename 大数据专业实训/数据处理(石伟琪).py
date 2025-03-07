import pandas as pd

diamonds_df = pd.read_csv(r'diamonds_数据集.csv')
# 显示前5行以了解其结构和内容
# print(diamonds_df.head())

missing_values = diamonds_df.isnull().sum()  # 检查数据集中是否有缺失值
# print(missing_values)

data_types = diamonds_df.dtypes  # 检查每列的数据类型
# print(data_types)

duplicate_rows = diamonds_df.duplicated().sum()  # 检查数据集中的重复行
if duplicate_rows > 0:  # 删除重复的行
    diamonds_df = diamonds_df.drop_duplicates()
# 显示删除后的重复项数和新的行数
# print(duplicate_rows, len(diamonds_df))

numerical_stats = diamonds_df.describe()  # 用于检查异常值的数值列的描述性统计信息
categorical_info = {col: diamonds_df[col].unique() for col in ['cut', 'color', 'clarity']}  # 用于检查任何异常的分类列的唯一值
# print(numerical_stats, categorical_info)

zero_dimensions = diamonds_df[(diamonds_df['x'] == 0) | (diamonds_df['y'] == 0) | (diamonds_df['z'] == 0)]
# 查找维度x、y或z为零的行和行数
# print(zero_dimensions,len(zero_dimensions))
# 删除维度 x、y 或 z 为零的行
diamonds_df_cleaned = diamonds_df.drop(zero_dimensions.index)
#  验证移除后的行数
# print(len(diamonds_df_cleaned))

# 再次检查数据集中的缺失值
missing2_values = diamonds_df_cleaned.isnull().sum()
# print(missing2_values)

# 将预处理后的数据写入新的 CSV 文件
cl_diamonds_df = r'diamonds_预处理后.csv'
diamonds_df.to_csv(cl_diamonds_df, index=False)
