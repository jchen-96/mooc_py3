origin=0
def visit(pos):
    def go(setup):
        nonlocal pos #、声明为非局部变量
        new_pos=pos+setup
        pos=new_pos
        return new_pos
    return go

f=visit(origin)
print(f(1))
print(f(2))
print(f(3))
