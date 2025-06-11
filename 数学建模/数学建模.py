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
            'k_L': 0.005,  # 脂肪代谢衰减系数(day⁻¹kg⁻¹)
            'k_T': 2.3e-5,  # 时间代谢衰减系数(day⁻²)
            'MET': 4.3,  # 运动强度(MET)
            't_a': 1.0,  # 每日运动时间(hours/day)
            'P_ratio': 0.3,  # 蛋白质供能比
            'C_ratio': 0.5,  # 碳水供能比
            'F_ratio': 0.2  # 脂肪供能比
        }

    def energy_equations(self, t, y):
        """耦合微分方程系统"""
        W, BMRb = y
        P = self.params['P_ratio'] * self.diet_intake(t)
        C = self.params['C_ratio'] * self.diet_intake(t)
        F = self.params['F_ratio'] * self.diet_intake(t)

        # 计算各项能量
        E_effective = P + C + F
        Γ = 1 + 0.15 * P / E_effective - 0.1 * F / E_effective
        η = 1.2 + 0.3 * np.tanh(0.1 * self.params['t_a'])
        E_activity = 4184 * self.params['MET'] * self.params['t_a'] * W * η

        # 微分方程
        dWdt = (E_effective - (BMRb * Γ + E_activity + 0.1 * E_effective)) / (32.2e6)
        dBMRbdt = -self.params['k_L'] * (self.params['W0'] - W) * BMRb - self.params['k_T'] * t * BMRb

        return [dWdt, dBMRbdt]

    def diet_intake(self, t):
        """随时间变化的饮食策略"""
        # 基础摄入：前30天 2000千卡/天，之后1800千卡
        base = 2000 * KCAL_TO_J if t < 30 else 1800 * KCAL_TO_J
        # 添加每周1天的欺骗日(增加20%摄入)
        if (t % 7) == 6:
            return base * 1.2
        return base

    def simulate(self, days=DAYS):
        """运行模拟"""
        t_span = (0, days)
        y0 = [self.params['W0'], self.params['BMRb0']]

        sol = solve_ivp(self.energy_equations, t_span, y0, method='RK45',
                        t_eval=np.linspace(0, days, days * 24), dense_output=True)
        return sol

# 确保matplotlib能够显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 使用黑体或者你系统中存在的其他中文字体
plt.rcParams['axes.unicode_minus'] = False
# 解决负号'-'显示为方块的问题
# 验证1：基础案例
model = MetabolismModel()
sol = model.simulate()

# 验证2：参数敏感性分析 - 运动时间对比
model_high_ex = MetabolismModel()
model_high_ex.params['t_a'] = 1.5
sol_high = model_high_ex.simulate()

# 验证3：理论验证(能量平衡时体重稳定)
model_balance = MetabolismModel()
model_balance.params['P_ratio'] = 0.25
model_balance.params['C_ratio'] = 0.55
model_balance.params['F_ratio'] = 0.2
model_balance.params['BMRb0'] = 6.8e6
# 调整初始代谢率
sol_balance = model_balance.simulate()

# 可视化结果
plt.figure(figsize=(12, 8))

# 体重变化曲线
plt.subplot(2, 2, 1)
plt.plot(sol.t / 7, sol.y[0], label='基础案例')
plt.plot(sol_high.t / 7, sol_high.y[0], '--', label='增加运动')
plt.plot(sol_balance.t / 7, sol_balance.y[0], ':', label='能量平衡')
plt.xlabel('时间(周)')
plt.ylabel('体重(kg)')
plt.title('体重变化趋势')
plt.grid(True)
plt.legend()

# 代谢率变化
plt.subplot(2, 2, 2)
plt.plot(sol.t / 7, sol.y[1] / 1e6, label='基础代谢率')
plt.xlabel('时间(周)')
plt.ylabel('基础代谢(MJ/day)')
plt.title('代谢适应过程')
plt.grid(True)

# 能量差分析
plt.subplot(2, 2, 3)
delta_E = [(model.diet_intake(t) - (BMRb * 1.1 + 4184 * model.params['MET'] * model.params['t_a'] * W * 1.2))
           for t, W, BMRb in zip(sol.t, sol.y[0], sol.y[1])]
plt.plot(sol.t / 7, np.array(delta_E) / KCAL_TO_J / 1000, 'r')  # 转换为千卡
plt.xlabel('时间(周)')
plt.ylabel('能量差(千卡/天)')
plt.title('每日能量缺口')
plt.grid(True)

# 运动效果对比
plt.subplot(2, 2, 4)
activity_base = 4184 * model.params['MET'] * model.params['t_a'] * sol.y[0] * 1.2
activity_high = 4184 * model_high_ex.params['MET'] * model_high_ex.params['t_a'] * sol_high.y[0] * 1.2
plt.plot(sol.t / 7, activity_base / KCAL_TO_J, label='基础运动')
plt.plot(sol.t / 7, activity_high / KCAL_TO_J, label='加强运动')
plt.xlabel('时间(周)')
plt.ylabel('运动消耗(千卡/天)')
plt.title('运动干预效果')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# 输出关键指标
print(f"基础案例最终体重: {sol.y[0, -1]:.1f} kg (-{model.params['W0'] - sol.y[0, -1]:.1f} kg)")
print(f"增加运动最终体重: {sol_high.y[0, -1]:.1f} kg (-{model.params['W0'] - sol_high.y[0, -1]:.1f} kg)")
print(f"能量平衡案例体重变化: {sol_balance.y[0, -1] - model_balance.params['W0']:.2f} kg")