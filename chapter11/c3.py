def f1():
    a=10
    def f2():
       # a=20# 这里如果定义了，就不是闭包了，闭包是函数加环境变量
    #    环境变量以为着要引用外部
        return a
    return f2


# 闭包里面的变量不会影响到外部的变量
f=f1()
print(f)
print(f.__closure__)