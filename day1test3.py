#1.使用列表推导式存储 1-100 的整数，然后输出其中所有偶数
# 直接生成1~100的偶数列表
evens = [x for x in range(1, 101) if x % 2 == 0]

print("1~100的偶数：", evens)


#2.给定一个列表，删除其中的重复元素并保持顺序不变。
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

# 示例
original_list = [3, 2, 1, 2, 4, 3, 5]
result = remove_duplicates(original_list)
print("去重后保持顺序：", result)  # 输出: [3, 2, 1, 4, 5]


#假设两个列表为 keys =["a","b","c”],values =[1,2,3]，将它们合并为一个字典并输出(第一个3列表为键，第二个列表为值)。
keys = ["a", "b", "c"]
values = [1, 2, 3]

# 合并为字典
merged_dict = dict(zip(keys, values))
print("合并后的字典：", merged_dict)


#4.定义一个元组存储学生信息(姓名，年龄，成绩)，然后解包并输出各字段。
# 定义学生信息元组
student = ("张三", 18, 90)

# 解包元组并输出
name, age, score = student
print(f"姓名：{name}, 年龄：{age}, 成绩：{score}")