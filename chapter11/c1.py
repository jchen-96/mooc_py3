from enum import Enum


# 声明一个枚举类
class VIP(Enum):
    yellow = 1
    green = 2
    black = 3
    red = 4

print(VIP.yellow)
