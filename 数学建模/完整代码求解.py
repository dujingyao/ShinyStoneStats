import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 常量定义
KCAL_TO_J = 4184  # 1千卡=4184焦耳
DAYS = 90  # 模拟时长(天)


class MetabolismModel:
    def __init__(self):
        # 模型参数
        self.params = {
            'W0': 80.0,  # 初始体重(kg)
            'BMRb0': 7.5e6,  # 初始基础代谢(J/day)
            'k_L': 0.005,  # 脂肪代谢衰减系数(day^-1·kg^-1)
            'k_T': 2.3e-5,  # 时间代谢衰减系数(day^-2)
            'MET': 4.3,  # 运动强度(MET)
            't_a': 1.0,  # 每日运动时间(hours/day)
            'P_ratio': 0.3,  # 蛋白质供能比
            'C_ratio': 0.5,  # 碳水供能比
            'F_ratio': 0.2,  # 脂肪供能比
            'diet': 8.0e6  # 日摄入总热量(J)
        }

    def equations(self, t, y):
        """耦合微分方程系统"""
        W, BMRb = y

        # 分解三大营养素
        P = self.params['P_ratio'] * self.params['diet']
        C = self.params['C_ratio'] * self.params['diet']
        F = self.params['F_ratio'] * self.params['diet']

        # 计算调节因子
        E_effective = P + C + F
        Γ = 1 + 0.15 * P / E_effective - 0.1 * F / E_effective
        η = 1.2 + 0.3 * np.tanh(0.1 * self.params['t_a'])

        # 活动消耗
        E_activity = 4184 * self.params['MET'] * self.params['t_a'] * W * η

        # 能量差计算
        dWdt = (E_effective - (BMRb * Γ + E_activity + 0.1 * E_effective)) / 32.2e6

        # 代谢率衰减
        ΔW = self.params['W0'] - W
        dBMRbdt = -self.params['k_L'] * ΔW * BMRb - self.params['k_T'] * t * BMRb

        return [dWdt, dBMRbdt]

    def simulate(self):
        # 设置中文显示
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # 求解微分方程
        sol = solve_ivp(self.equations,
                        [0, DAYS],
                        [self.params['W0'], self.params['BMRb0']],
                        method='RK45',
                        dense_output=True)

        return sol


# 模型验证
model = MetabolismModel()
sol = model.simulate()

# 可视化结果
t = np.linspace(0, DAYS, 1000)
W, BMRb = sol.sol(t)

plt.figure(figsize=(14, 8))

# 体重变化曲线
plt.subplot(2, 2, 1)
plt.plot(t / 7, W, label='模拟体重')
plt.xlabel('时间(周)')
plt.ylabel('体重(kg)')
plt.title('体重变化趋势')
plt.grid(True)

# 代谢率变化
plt.subplot(2, 2, 2)
plt.plot(t / 7, BMRb / 1e6)
plt.xlabel('时间(周)')
plt.ylabel('基础代谢率(MJ/day)')
plt.title('代谢适应过程')
plt.grid(True)

# 能量差分析
E_intake = model.params['diet'] * np.ones_like(t)
E_activity = 4184 * model.params['MET'] * model.params['t_a'] * W * (1.2 + 0.3 * np.tanh(0.1 * model.params['t_a']))
E_TEF = 0.1 * (E_intake - (E_intake * 0.2))  # 膳食纤维占比20%
E_out = BMRb * (1 + 0.15 * 0.3 - 0.1 * 0.2) + E_activity + E_TEF
delta_E = (E_intake - E_out) / KCAL_TO_J / 1000  # 转换为千卡

plt.subplot(2, 2, 3)
plt.plot(t / 7, delta_E)
plt.axhline(0, color='r', linestyle='--')
plt.xlabel('时间(周)')
plt.ylabel('日能量差(千卡)')
plt.title('每日能量缺口变化')
plt.grid(True)

# 参数敏感性分析
model_high = MetabolismModel()
model_high.params['t_a'] = 1.5
sol_high = model_high.simulate()

plt.subplot(2, 2, 4)
plt.plot(t / 7, W, label='基础方案')
plt.plot(t / 7, sol_high.sol(t)[0], '--', label='增加运动')
plt.xlabel('时间(周)')
plt.ylabel('体重(kg)')
plt.title('不同运动方案的减重效果')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()