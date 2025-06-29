#1编写一个函数，判断一个数是否为回文数（例如：121是回文数，123不是）。
def is_palindrome(num):
    """判断一个整数是否为回文数"""
    num_str = str(num)
    return num_str == num_str[::-1]

# 测试
print(is_palindrome(121))  # True
print(is_palindrome(123))  # False


#2编写一个函数，接受任意数量的参数，返回它们的平均值。
def average(*args):
    """计算任意数量参数的平均值"""
    return sum(args) / len(args) if args else 0

# 测试
print(average(1, 2, 3, 4))  # 2.5
print(average(10, 20))      # 15.0


#3定义一个函数，接收任意多个字符串，返回最长的字符串。
def longest_string(*strings):
    """返回多个字符串中最长的一个"""
    return max(strings, key=len, default=None)

# 测试
print(longest_string("apple", "banana", "cherry"))  # "banana"
print(longest_string("a", "bc", "def"))            # "def"


#创建一个模块，包含计算矩形面积和周长的函数，并在另一个文件中导入使用。
def area(length, width):
    """计算矩形面积"""
    return length * width

def perimeter(length, width):
    """计算矩形周长"""
    return 2 * (length + width)