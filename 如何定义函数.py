'''
1、如何定义函数
2、函数内部需要外部的资源：通过函数的参数来实现
3、函数执行后的结果需要告诉外界：通过返回值告诉给外界
'''



# a = 10
# b = 20
# def fn(a, b):
#     # pass
#     return a + b
# print(fn(1, 3))
#
# def add(n1, n2):
#     return n1 + n2


# 加减乘除案例
def add(n1, n2):
    return n1 + n2


def low(n1, n2):
    return n1 - n2


def jump(n1, n2):
    return n1 * n2


def full(n1, n2):
    return n1 / n2


def computed(n1, n2, cmd):
    if cmd == 'add':
        return add(n1, n2)
    elif cmd == 'low':
        return low(n1, n2)
    elif cmd == 'jump':
        return jump(n1, n2)
    elif cmd == 'full':
        return full(n1, n2)

res = computed(13, 21, 'full')
print(type(res))
