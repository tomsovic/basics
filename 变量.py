# 一. 变量

# 如何定义变量？

# 变量名（相当于门牌号，指向值所在的空间），等号，变量值
name = 'Egon'
sex = 'male'
age = 18
level = 10

# 变量的定义规范
# 1. 变量名只能是字母、数字或下划线的任意组合
# 2. 变量名的第一个字符不能使数字
# 3. 关键字不能声明为变量名 ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
#  'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import',
#  'in', 'is', 'lambad', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while',
#  'whit', 'yield']

# 定义方式
# 驼峰体
AgeOfOldboy = 56
NumberOfStudents = 60
# 下划线(推荐使用)
age_of_oldboy = 56
number_of_students = 80

# 定义变量名不好的方式
# 1. 变量名为中文，拼音
# 2. 变量名过长
# 3. 变名词不达意


# 定义比那里会有: id , type, value

# 1. 等号比较的是 volue
# 2. is 比较的是 id

# 强调：
# 1. id相同，意味着 type和volue毕竟相同
# 2. volue相同type肯定相同，但id可能不同，如下：

x = 'Info Egon:18'
y = 'Info EgonL18'
id(x)
id(y)
x == y
x is y








