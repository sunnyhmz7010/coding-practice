price = 19
a, b = map(int,input().split())

n = (a*10+b)//price
print(n)

"""
为什么必须拆分输入？
input() 读入的是整行纯文本 "10 3"。
Python 无法直接将包含空格的字符串 "10 3" 转换为单个整数。
.split() 会将其切分成列表 ['10', '3']，配合 map(int, ...) 即可分别赋给变量 a 和 b。
"""