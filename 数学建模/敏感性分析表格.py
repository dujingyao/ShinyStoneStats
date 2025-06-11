from tabulate import tabulate

from 数学建模.完整代码求解 import MetabolismModel

# 生成敏感性分析数据
scenarios = [
    ("基础案例", 1.0, 0.3, 0.5, 0.2),
    ("增加运动", 1.5, 0.3, 0.5, 0.2),
    ("高蛋白饮食", 1.0, 0.4, 0.4, 0.2),
    ("低碳水饮食", 1.0, 0.3, 0.3, 0.4)
]

results = []
for desc, t_a, p, c, f in scenarios:
    model = MetabolismModel()
    model.params.update({'t_a':t_a, 'P_ratio':p, 'C_ratio':c, 'F_ratio':f})
    sol = model.simulate()
    final_w = sol.y[0][-1]
    results.append([desc, f"{final_w:.1f}kg", f"{(model.params['W0']-final_w):.1f}kg"])

print(tabulate(results,
               headers=["场景", "最终体重", "总减重"],
               tablefmt="grid"))