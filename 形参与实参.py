# 形参与实参
# def fn(a, b=10, *args, c, d=20, e, **kwargs):
#     pass

a = 100
b = '200'

def fn1(a, b): #形参：在函数定义时（）里面出现的参数
    print(a, b)

fn1(a, '2000') #实参： 在函数调用时 （）里面出现的参数
# 函数调用传参： 将实参的值赋值给形参
# 实参有实际意义
# 形参本身没有实际值，在函数调用时，传入什么实参，形参就装有什么值
print('end')

