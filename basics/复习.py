# age = int(input('请输入年龄：'))
# # print(age)
# # print("去相亲")
# # print("阿姨好，打扰了")
#
# if age <=18:
#     print("去相亲")
# else:
#     print("阿姨好，打扰了")


# price = int(input("phone price:"))
# if price > 15000:
#     print("不考虑")
# elif price > 10000:
#     print("观望")
# else:
#     print("入手！")


# 案例：登录
# username = input("请输入账号：")
#
# # owen = 123
# if username == 'owen':
#     pwd = input("请输入你的密码：")
#     if pwd == '123':
#         print('登录成功')
#     else:
#         print('密码错误')
# else:
#     print('账号不存在')

# 循环

# 循环语法
'''
while 条件：
    代码块
# 原理： 当条件为真，执行代码块，到条件为假，结束该循环
'''

# 计数器
# count = 1
# while count <= 5:
#     print("egon最衰")
#     count += 1
#

res = 1
num = 1
while num <= 100:
    if num % 7 == 0:
        res = num
    num += 1
print(res)
