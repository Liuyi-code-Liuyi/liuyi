#1.
s1 = "Python is a powerful programming language"
words = s1.split()  # 默认按空格分割
last_word = words[-1]  # 取最后一个单词
print("最后一个单词：", last_word)  # 输出: language

s2 = " Let's learn together"
combined = s1 + s2  # 连接字符串
print((combined + "\n") * 3)  # 重复3次，每次换行


words = s1.split()
p_words = [word for word in words if word.lower().startswith('p')]
print("以p/P开头的单词：", p_words)  # 输出: ['Python', 'powerful', 'programming']

#2.
s3 = " Hello, World! This is a test string. "

# 操作1
stripped = s3.strip()
print("去除前后空格：", stripped)

# 操作2
uppercase = stripped.upper()
print("转换为大写：", uppercase)

# 操作3
index = stripped.find("test")
print("'test'的起始下标：", index)

# 操作4
replaced = stripped.replace("test", "practice")
print("替换后：", replaced)

# 操作5
joined = "-".join(replaced.split())
print("分割并连接：", joined)