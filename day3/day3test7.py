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
