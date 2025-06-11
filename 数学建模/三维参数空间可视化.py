import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from 数学建模.完整代码求解 import MetabolismModel

# 生成参数网格
t_a_values = np.linspace(0.5, 2.0, 20)
p_ratio = np.linspace(0.2, 0.4, 20)
X, Y = np.meshgrid(t_a_values, p_ratio)
Z = np.zeros_like(X)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        model = MetabolismModel()
        model.params['t_a'] = X[i,j]
        model.params['P_ratio'] = Y[i,j]
        model.params['C_ratio'] = 0.5 - (Y[i,j]-0.3)
        model.params['F_ratio'] = 1 - model.params['P_ratio'] - model.params['C_ratio']
        sol = model.simulate()
        Z[i,j] = model.params['W0'] - sol.y[0][-1]

# 绘制三维曲面
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('运动时间(h/day)')
ax.set_ylabel('蛋白质供能比')
ax.set_zlabel('总减重(kg)')
ax.set_title('参数空间响应曲面')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()