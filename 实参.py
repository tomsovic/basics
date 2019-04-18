def fn(a, b):
    print(a, b)

# 实参：
# 1.位置实参： 按位置先后进行传参，a, b不能被颠倒位置进行传参，a永远比b先接受受值
fn(10, 20)
fn(20, 10)

a = 100
b = 200
fn(a, b)
fn(b, a)

#传参两种方式： 实参名 | 实参值

# 2. 关键字参数： 指名道姓进行传参， a,b能被颠倒位置进行传参，名字指向谁，就是谁接受值
c = 1000
fn(a = 10, b = c)
fn(b = 20, a = 10)

# 传参两种方式： 形参名 = 实参名 | 形参名 = 实参值


# 结合传参
def func(a, b, c):
    print(a, b, c)

# func(10, b=20, 200) 报错：SyntaxError: positional argument follows keyword argument
# 两种实参在一起传参时：必须位置在前，关键字在后