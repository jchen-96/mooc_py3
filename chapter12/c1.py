import time


def deactor(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper
@deactor
def f1():
    print('this is a function f1')


f1()
