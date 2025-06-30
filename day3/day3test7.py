import numpy as np
import matplotlib.pyplot as plt

# 创建x值，从-10到10，间隔为0.1
x = np.linspace(-10, 10, 400)

# 计算y值
y = x**3

# 创建图形
plt.figure(figsize=(6, 6))

# 绘制曲线
plt.plot(x, y, label="y = x^3")

# 添加标题和标签
plt.title("Graph of y = x^3")
plt.xlabel("x")
plt.ylabel("y")

# 添加网格
plt.grid(True)

# 显示图例
plt.legend()

# 显示图形
plt.show()

year = np.arange(2000, 2021).astype(np.str_)
month = np.random.randint(1, 13, size=20).astype(np.str_)
day = np.random.randint(1, 31, size=20).astype(np.str_)
date = np.array([])

for i in range(20):
    a = np.array([year[i], month[i], day[i]])
    b = ['/'.join(a)]  # 组合年月日
    date = np.append(date, b)

# 随机销量
sales = np.random.randint(500, 2000, size=len(date))

# 绘制图形
plt.xticks(range(0, len(date), 2), ['日期:%s' % i for i in date][::2], rotation=45, color='red')
plt.plot(date, sales)


plt.show()