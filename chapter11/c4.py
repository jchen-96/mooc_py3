
start=0

# def visit():
#     def go(step):
#         start+=step
#         return start
#     return go

def go(setp):
    global start #只能这样声明，否则默认等号左边是局部变量
    new_s=start+setp
    start=new_s
    return new_s

print(go(2))
print(go(4))