import matplotlib.pyplot as plt

# 设置中文字体（例如 SimHei）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
most_common_words= [('数字化', 22), ('技术装备', 14),('智能化',11),('农产品',7),('因地制宜',6),('信息化',5),('机器人',4),('推广应用',4),('大力发展',3),('贯彻落实',3),('信息技术',3),('全方位',3),('现代化',3),('农业产业',3),('核心技术',3)]
# 绘制柱状图
words = [word for word, count in most_common_words]
counts = [count for word, count in most_common_words]

plt.bar(words, counts)

plt.xlabel("关键词")

plt.ylabel("词频")

plt.title("关键词词频统计")

plt.xticks(rotation=45, ha="right")

plt.show()