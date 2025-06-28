#1.编写程序，输出1到100之间的所有素数。(只能被1和自身整除的数)
def is_prime(n):
    """判断一个数是否为素数"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # 只需检查到平方根
        if n % i == 0:
            return False
    return True

# 输出1~100的素数
primes = [x for x in range(1, 101) if is_prime(x)]
print("1~100的素数：", primes)

#2.计算斐波那契数列的前20项(斐波那契数列:0,1,1,2,3,5,8..，第一项为0，第二项为1，后面的项都是前面两项之和)。
def fib_recursive(n):
    """递归实现（仅用于理解，n>30时极慢）"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# 输出前20项（递归法逐个计算）
fib_20_rec = [fib_recursive(i) for i in range(20)]
print("递归法结果：", fib_20_rec)  # 与方法1结果一致


#3使用 while 循环计算 1-10000 之间能被3整除或者能被5整除且不能被15整除的数的和。
total = 0
num = 1
while num <= 10000:
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        total += num
    num += 1
print("满足条件的数的和：", total)