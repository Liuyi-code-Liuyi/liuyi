import pandas as pd

# 读取三个CSV文件
file_2015 = pd.read_csv(r'D:\下载\python各种\PythonProject4\day3\year_data\2015年国内主要城市年度数据.csv')
file_2016 = pd.read_csv(r'D:\下载\python各种\PythonProject4\day3\year_data\2016年国内主要城市年度数据.csv')
file_2017 = pd.read_csv(r'D:\下载\python各种\PythonProject4\day3\year_data\2017年国内主要城市年度数据.csv')

# 1. 合并数据，纵向连接
merged_df = pd.concat([file_2015, file_2016, file_2017], ignore_index=True)

# 打印合并后的数据的列名，检查是否存在“地区”，“年份”，“国内生产总值”，“社会商品零售总额”等
print("合并后的数据的列名：")
print(merged_df.columns)

# 清理列名：去掉空格并转换为小写
merged_df.columns = merged_df.columns.str.strip().str.lower()

# 打印清理后的列名，确认列名已转化为小写
print("\n清理后的列名：")
print(merged_df.columns)

# 2. 计算每个地区2015-2017年国内生产总值的年均增长率，并找出增长率最高和最低的五个地区
try:
    gdp_by_region_year = merged_df[['地区', '年份', '国内生产总值']]  # 根据实际列名调整
    gdp_pivot = gdp_by_region_year.pivot(index='地区', columns='年份', values='国内生产总值')

    # 计算年均增长率
    gdp_pivot['年均增长率'] = (gdp_pivot[2017] - gdp_pivot[2015]) / gdp_pivot[2015] / 2 * 100  # 年均增长率百分比

    # 找出增长率最高和最低的五个地区
    top_5_growth = gdp_pivot['年均增长率'].nlargest(5)
    bottom_5_growth = gdp_pivot['年均增长率'].nsmallest(5)

    print("\n增长率最高的五个地区：")
    print(top_5_growth)
    print("\n增长率最低的五个地区：")
    print(bottom_5_growth)
except KeyError as e:
    print(f"找不到列：{e}")

# 3. 对医院、卫生院数进行归一化处理（Min-Max标准化），并按年份比较各地区医疗资源的变化
if '医院、卫生院数' in merged_df.columns:
    merged_df['医院、卫生院数归一化'] = (merged_df['医院、卫生院数'] - merged_df['医院、卫生院数'].min()) / (merged_df['医院、卫生院数'].max() - merged_df['医院、卫生院数'].min())

    # 按年份比较各地区医疗资源变化
    hospital_change = merged_df[['地区', '年份', '医院、卫生院数归一化']].pivot_table(index='地区', columns='年份', values=['医院、卫生院数归一化'])

    print("\n各地区医疗资源变化：")
    print(hospital_change)
else:
    print("\n没有找到'医院、卫生院数'列，请检查数据。")

# 4. 提取北京、上海、广州、深圳四个地区2015-2017年GDP和社会商品零售总额数据，用新的csv呈现，并保存
regions = ['北京', '上海', '广州', '深圳']
try:
    filtered_df = merged_df[merged_df['地区'].isin(regions)][['地区', '年份', '国内生产总值', '社会商品零售总额']]
    # 保存为新的CSV文件
    output_file = r'D:\下载\python各种\PythonProject4\day3\year_data\new.csv'
    filtered_df.to_csv(output_file, index=False)
    print(f"\n提取的四个地区的数据已保存为新的CSV文件: {output_file}")
except KeyError as e:
    print(f"找不到列：{e}")
