#1、定义一个 Car 类，包含 brand（品牌）和 speed（速度）属性，以及 accelerate（加速，速度增加 m 次，每次增加 10）和 brake（刹车，速度减少 n次，每次减少10，不低于 0）方法
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand  # 品牌
        self.speed = speed  # 速度（默认0）

    def accelerate(self, m):
        """加速：m次，每次速度+10"""
        self.speed += 10 * m
        return self.speed

    def brake(self, n):
        """刹车：n次，每次速度-10（最低为0）"""
        self.speed = max(0, self.speed - 10 * n)
        return self.speed

#2、创建 Car 类的实例，调用加速和刹车方法，输出当前速度
# 创建实例
my_car = Car("Tesla", 30)

# 测试加速和刹车
print(f"当前速度：{my_car.speed}")          # 输出: 30
print(f"加速2次后：{my_car.accelerate(2)}") # 输出: 50 (30 + 10*2)
print(f"刹车3次后：{my_car.brake(3)}")      # 输出: 20 (50 - 10*3, 不低于0)


#3、定义 ElectricCar 子类继承 Car，新增 battery（电量）属性和 charge（充电，电量增加 20，不超过 100）方法。
class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        super().__init__(brand, speed)  # 继承父类属性
        self.battery = battery  # 新增电量属性（默认50）

    def charge(self):
        """充电：电量+20（不超过100）"""
        self.battery = min(100, self.battery + 20)
        return self.battery

# 创建电动车实例
e_car = ElectricCar("NIO", 40, 60)

# 测试继承和方法
print(f"品牌：{e_car.brand}")             # 输出: NIO
print(f"当前速度：{e_car.speed}")         # 输出: 40
print(f"充电后电量：{e_car.charge()}")     # 输出: 80 (60 + 20)
print(f"加速1次后：{e_car.accelerate(1)}") # 输出: 50 (40 + 10*1)