import pandas as pd
import os

# 确保datas目录存在
os.makedirs('datas', exist_ok=True)

# 读取名医榜数据
try:
    df = pd.read_csv('doctor_skills.csv')
    print(f"读取到{len(df)}条原始数据")
except FileNotFoundError:
    try:
        df = pd.read_csv('名医榜.csv')
        print(f"读取到{len(df)}条原始数据")
    except FileNotFoundError:
        print("无法找到'doctor_skills.csv'或'名医榜.csv'文件")
        exit(1)

# 确保列名符合要求
if 'name' in df.columns and 'skill' in df.columns:
    df.columns = ['姓名', '擅长领域']
elif '姓名' not in df.columns or '擅长领域' not in df.columns:
    print("CSV文件列名不符合要求，需要包含'姓名'和'擅长领域'列")
    exit(1)

# 数据清洗：删除空值
df_cleaned = df.dropna()
print(f"删除空值后剩余{len(df_cleaned)}条数据")

# 数据清洗：删除重复值
df_cleaned = df_cleaned.drop_duplicates()
print(f"删除重复值后剩余{len(df_cleaned)}条数据")

# 添加时间列
df_cleaned['时间'] = '2024-06'

# 保存清洗后的数据
output_path = 'datas/清洗结果.csv'
df_cleaned.to_csv(output_path, index=False, encoding='utf-8')
print(f"数据清洗完成，结果已保存至{output_path}")