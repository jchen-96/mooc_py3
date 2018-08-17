def curve_pre():
    a=25 # 这里注释了就可以
    def curve(x):
        return a*x*x
    return curve


a=10 #没啥用

f=curve_pre()

print(f(5))

print(f.__closure__[0].cell_contents)
# 闭包=函数+环境变量(定义时候的变量不是全局变量)
# 保存了一个现场