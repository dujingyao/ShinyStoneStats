# 读取“名医榜.csv”，数据列名为：姓名和擅长领域，删除数据项为空的数据，
# 删除重复数据，增加“时间”列，数据为“2024-06”，
# 结果存放到“清洗结果.csv”中，保存在datas目录。
# 数据清晰流程总结
# 1. 导入库 pandas和os
# 2. 确保datas目录存在
# 3. 读取名医榜数据 pd=pd.read_csv('需要预处理的文件名称.csv')
# 4. 确保列名符合要求
    # if 'name' in df.columns and 'skill' in df.columns:
    #     df.columns = ['姓名', '擅长领域']
    # elif '姓名' not in df.columns or '擅长领域' not in df.columns:
    #     print("CSV文件列名不符合要求，需要包含'姓名'和'擅长领域'列")
    #     exit(1)
# 5. 数据清洗：删除空值 df_cleaned = df.dropna()
# 6. 数据清洗：删除重复值 df_cleaned = df_cleaned.drop_duplicates()
# 7. 添加时间列 df_cleaned['时间'] = '2024-06'
# 8. 保存清洗后的数据 df_cleaned.to_csv('datas/清洗结果.csv', index=False, encoding='utf-8')
import pandas as pd
import os

# 确保datas目录存在
os.makedirs('datas', exist_ok=True)

# 读取名医榜数据
df = pd.read_csv('doctor_skills.csv')

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