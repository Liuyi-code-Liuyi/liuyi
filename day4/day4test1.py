import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.family'] = 'SimHei'  # 使用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 国家列表
countries = ['挪威', '德国', '中国', '美国', '瑞典']

# 奖牌数量
gold_medal = np.array([16, 12, 9, 8, 8])
silver_medal = np.array([8, 10, 4, 10, 5])
bronze_medal = np.array([13, 5, 2, 7, 5])

# x轴位置
x = np.arange(len(countries))

# 设置x轴标签
plt.xticks(x, countries)

# 绘制柱状图
plt.bar(x - 0.2, gold_medal, width=0.2, color="gold", label="金牌")
plt.bar(x, silver_medal, width=0.2, color="silver", label="银牌")
plt.bar(x + 0.2, bronze_medal, width=0.2, color="saddlebrown", label="铜牌")

# 添加数值标签（文本）
for i in x:
    plt.text(x[i] - 0.2, gold_medal[i], gold_medal[i], va='bottom', ha='center', fontsize=8)
    plt.text(x[i], silver_medal[i], silver_medal[i], va='bottom', ha='center', fontsize=8)
    plt.text(x[i] + 0.2, bronze_medal[i], bronze_medal[i], va='bottom', ha='center', fontsize=8)

# 添加图例和标题
plt.legend()
plt.title("各国奖牌数量对比柱状图")
plt.ylabel("奖牌数")

# 显示图形
plt.tight_layout()
plt.show()
