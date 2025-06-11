import pandas as pd
import numpy as np
import re

# 1. 读取数据
# 读取安居客数据
try:
    anjuke_df = pd.read_csv('anjuke.csv', encoding='utf-8')
    print("安居客数据读取成功，共{}行".format(len(anjuke_df)))
    print(anjuke_df.head(2))
except Exception as e:
    print("安居客数据读取失败:", e)
    anjuke_df = pd.DataFrame()

# 读取贝壳网数据
try:
    beike_df = pd.read_csv('house_data.csv', header=None, encoding='utf-8')
    beike_df.columns = ['地址', '楼盘', '单价', '总价范围']
    print("贝壳数据读取成功，共{}行".format(len(beike_df)))
    print(beike_df.head(2))
except Exception as e:
    print("贝壳数据读取失败:", e)
    beike_df = pd.DataFrame()

# 2. 数据预处理 - 安居客数据
if not anjuke_df.empty:
    # 复制数据，避免SettingWithCopyWarning
    anjuke_clean = anjuke_df.copy()

    # 去重
    anjuke_clean = anjuke_clean.drop_duplicates()

    # 提取价格数字(假设价格格式为"xxxx元/平")
    anjuke_clean['价格数值'] = anjuke_clean['价格'].str.extract(r'(\d+)').astype(float)

    # 提取面积数字(假设面积格式为"xx平米")
    anjuke_clean['面积数值'] = anjuke_clean['面积'].str.extract(r'(\d+\.?\d*)').astype(float)

    print("安居客数据清洗后：", anjuke_clean.shape)

# 3. 数据预处理 - 贝壳数据
if not beike_df.empty:
    # 复制数据，避免SettingWithCopyWarning
    beike_clean = beike_df.copy()

    # 去重
    beike_clean = beike_clean.drop_duplicates()

    # 将单价转换为数值型
    beike_clean['单价数值'] = pd.to_numeric(beike_clean['单价'], errors='coerce')

    # 从总价范围中提取最小价格和最大价格
    def extract_price_range(price_str):
        if isinstance(price_str, str):
            # 提取数字部分
            numbers = re.findall(r'\d+', price_str)
            if len(numbers) >= 1:
                min_price = float(numbers[0])
                max_price = float(numbers[-1] if len(numbers) > 1 else numbers[0])
                return pd.Series([min_price, max_price])
        return pd.Series([np.nan, np.nan])

    # 提取价格范围
    price_range = beike_clean['总价范围'].apply(extract_price_range)
    beike_clean['最小总价'] = price_range[0]
    beike_clean['最大总价'] = price_range[1]

    print("贝壳数据清洗后：", beike_clean.shape)

# 4. 统一数据格式并合并
# 准备合并的安居客数据
if not anjuke_df.empty:
    anjuke_merged = anjuke_clean[['楼盘', '地址', '价格数值', '面积数值']].copy()
    anjuke_merged.columns = ['楼盘名称', '地址', '单价', '面积']
    anjuke_merged['数据来源'] = '安居客'

# 准备合并的贝壳数据
if not beike_df.empty:
    beike_merged = beike_clean[['楼盘', '地址', '单价数值']].copy()
    beike_merged.columns = ['楼盘名称', '地址', '单价']
    beike_merged['数据来源'] = '贝壳'

# 合并数据
if not anjuke_df.empty and not beike_df.empty:
    merged_data = pd.concat([anjuke_merged, beike_merged], ignore_index=True)
else:
    merged_data = anjuke_merged if not anjuke_df.empty else beike_merged

# 5. 再次去重和清洗
if not merged_data.empty:
    # 去重，保留第一个出现的记录
    merged_data = merged_data.drop_duplicates(subset=['楼盘名称', '地址'], keep='first')

    # 移除单价为NaN的记录
    merged_data = merged_data.dropna(subset=['单价'])

    # 检查异常值（使用箱线图方法）
    Q1 = merged_data['单价'].quantile(0.25)
    Q3 = merged_data['单价'].quantile(0.75)
    IQR = Q3 - Q1

    # 过滤掉异常值
    merged_data = merged_data[(merged_data['单价'] >= (Q1 - 1.5 * IQR)) &
                             (merged_data['单价'] <= (Q3 + 1.5 * IQR))]

    print("合并后的数据：", merged_data.shape)
    print(merged_data.head())

    # 保存结果
    merged_data.to_csv('merged_house_data.csv', index=False, encoding='utf-8')
    print("合并数据已保存至merged_house_data.csv")
else:
    print("没有可合并的数据")