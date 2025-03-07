# 导入必要的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# 设置matplotlib以支持中文显示
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 1. 数据加载
# 读取数据集
data = pd.read_csv('diamonds_预处理后.csv')

# 2. 数据探索
# 查看数据的前几行
print(data.head())

# 查看数据的信息，包括数据类型和缺失值
print(data.info())

# 检查缺失值
print(data.isnull().sum())

# 3. 数据预处理
# 定义分类变量和数值变量
categorical_cols = ['cut', 'color', 'clarity']
numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']

# 使用ColumnTransformer进行预处理
# 对分类变量进行独热编码，对数值变量进行标准化
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first'), categorical_cols),
        ('num', StandardScaler(), numerical_cols)
    ]
)

# 4. 特征选择和目标变量选择
X = data.drop('price', axis=1)
y = data['price']

# 5. 数据分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. 模型选择和训练
# 创建一个包含预处理和模型的管道
model_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# 6.1 使用交叉验证评估模型
cv_scores = cross_val_score(model_pipeline, X, y, cv=5, scoring='r2')
print('交叉验证 R² 分数:', cv_scores)
print('平均交叉验证 R² 分数:', np.mean(cv_scores))

# 6.2 训练模型
model_pipeline.fit(X_train, y_train)

# 7. 预测
# 在测试集上进行预测
y_pred = model_pipeline.predict(X_test)

# 8. 模型评估
# 计算均方误差和R²分数
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('均方误差 (MSE):', mse)
print('测试集 R² 分数:', r2)

# 8.1 检查训练集上的性能
y_train_pred = model_pipeline.predict(X_train)
r2_train = r2_score(y_train, y_train_pred)
print('训练集 R² 分数:', r2_train)

# 9. 特征重要性分析
# 获取线性回归模型的系数
coefficients = model_pipeline.named_steps['regressor'].coef_
# 获取特征名称
feature_names = preprocessor.transformers_[0][1].get_feature_names_out(categorical_cols).tolist() + numerical_cols
# 创建系数 DataFrame
coef_df = pd.DataFrame({'特征': feature_names, '系数': coefficients})
print(coef_df)

# 10. 残差分析
# 计算残差
residuals = y_test - y_pred
# 绘制残差直方图
sns.histplot(residuals, kde=True)
plt.title('残差分布')
plt.xlabel('残差')
plt.ylabel('频数')
plt.savefig('残差直方图.png')
plt.close()
# plt.show()
