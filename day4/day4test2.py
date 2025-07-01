import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 设置中文显示
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取合并后的数据
df = pd.read_csv(r'D:\下载\python各种\PythonProject4\day3\year_data\hebing.csv')

# 按年份和地区提取GDP数据
pivot_df = df.pivot(index='地区', columns='年份', values='国内生产总值')

# 绘图
pivot_df.plot(kind='bar', figsize=(15, 7))
plt.title("2015-2017年各城市国内生产总值对比")
plt.xlabel("城市")
plt.ylabel("GDP（亿元）")
plt.legend(title="年份")
plt.tight_layout()
plt.show()
# 筛选2015年的数据
df_2015 = df[df['年份'] == 2015]

# 选取前10个城市（避免城市太多饼图不好看）
df_2015_top10 = df_2015.sort_values(by='国内生产总值', ascending=False).head(10)

# 绘图
plt.figure(figsize=(8, 8))
plt.pie(df_2015_top10['国内生产总值'], labels=df_2015_top10['地区'], autopct='%1.1f%%', startangle=140)
plt.title("2015年各城市GDP前10的城市占比")
plt.axis('equal')
plt.show()
