#1.判断变量x= 10, y="10",z= True 的数据类型并输出。
x = 10
y = "10"
z = True

# 判断数据类型并输出
print(f"x 的数据类型是：{type(x)}")
print(f"y 的数据类型是：{type(y)}")
print(f"z 的数据类型是：{type(z)}")

#2.接收用户输入的半径，输出圆的面积，π定义为3.14.
# 定义π的值
PI = 3.14

# 接收用户输入的半径（转换为浮点数）
radius = float(input("请输入圆的半径："))

# 计算圆的面积：面积 = π * r²
area = PI * (radius ** 2)

# 输出结果
print(f"半径为 {radius} 的圆的面积是：{area}")


#3.将字符串"3.14"转换为浮点数，再转换为整数，观察结果差异,
# 原始字符串
num_str = "3.14"

# 转换为浮点数
num_float = float(num_str)
print(f"转换为浮点数: {num_float}, 类型: {type(num_float)}")  # 输出: 3.14, float

# 转换为整数（直接截断小数部分）
num_int = int(num_float)
print(f"转换为整数: {num_int}, 类型: {type(num_int)}")  # 输出: 3, int





