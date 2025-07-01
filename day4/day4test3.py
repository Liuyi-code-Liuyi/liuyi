import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体支持
rcParams['font.family'] = 'SimHei'  # 黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取 Titanic 数据
df = pd.read_csv(r'D:\下载\python各种\PythonProject4\day4\train.csv')

# 去除缺失年龄的数据
df = df.dropna(subset=['Age'])

# 按年龄段分组（自定义年龄区间）
bins = [0, 10, 20, 30, 40, 50, 60, 100]
labels = ['0-10岁', '11-20岁', '21-30岁', '31-40岁', '41-50岁', '51-60岁', '60岁以上']
df['年龄段'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# 按年龄段计算生还率
age_survival_rate = df.groupby('年龄段')['Survived'].mean()

# 绘图
plt.figure(figsize=(10, 6))
plt.bar(age_survival_rate.index, age_survival_rate.values, color='lightgreen')

plt.title('不同年龄段的生还率')
plt.xlabel('年龄段')
plt.ylabel('生还率')
plt.ylim(0, 1)

# 添加数值标签
for i, rate in enumerate(age_survival_rate):
    plt.text(i, rate + 0.02, f"{rate:.2f}", ha='center', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
