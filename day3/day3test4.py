import pandas as pd

# 读取CSV文件
file_path = r'D:\下载\python各种\PythonProject4\day3\exercise_data\drinks.csv'
df = pd.read_csv(file_path)

# 1. 哪个大陆平均消耗的啤酒(beer)更多？
avg_beer_consumption = df.groupby('continent')['beer_servings'].mean()
continent_with_more_beer = avg_beer_consumption.idxmax()  # 获取啤酒消耗最多的大陆
print(f"平均消耗啤酒最多的大陆是：{continent_with_more_beer}")

# 2. 打印出每个大陆的红酒消耗(wine_servings)的描述性统计值
wine_stats = df.groupby('continent')['wine_servings'].describe()
print("\n每个大陆的红酒消耗的描述性统计值：")
print(wine_stats)

# 3. 打印出每个大陆每种酒类别的消耗平均值
avg_consumption_by_continent = df.groupby('continent')[['beer_servings', 'wine_servings', 'spirit_servings']].mean()
print("\n每个大陆每种酒类别的消耗平均值：")
print(avg_consumption_by_continent)

# 4. 打印出每个大陆每种酒类别的消耗中位数
median_consumption_by_continent = df.groupby('continent')[['beer_servings', 'wine_servings', 'spirit_servings']].median()
print("\n每个大陆每种酒类别的消耗中位数：")
print(median_consumption_by_continent)
