import pandas as pd
import numpy as np

# 1. 创建包含数据的 DataFrame
data = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Score': [85, 92, None, 88, 76],
    'Grade': ['A', 'A', 'B', 'B', 'C']
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 将 DataFrame 保存为 CSV 文件
df.to_csv(r'D:\下载\python各种\PythonProject4\day3\students.csv', index=False)

# 2. 读取 CSV 文件并打印前 3 行
df_read = pd.read_csv(r'D:\下载\python各种\PythonProject4\day3\students.csv')
print("前 3 行数据：")
print(df_read.head(3))

# 3. 填充缺失值
# 填充 Score 列的缺失值为平均分
mean_score = df_read['Score'].mean()
df_read['Score'] = df_read['Score'].fillna(mean_score)

# 填充 Name 列的缺失值为 "Unknown"
df_read['Name'] = df_read['Name'].fillna('Unknown')

# 4. 保存处理后的 DataFrame 为新的 CSV 文件
df_read.to_csv(r'D:\下载\python各种\PythonProject4\day3\students_cleaned.csv', index=False)

print("\n处理后的数据已保存为 'students_cleaned.csv'")
