# coding=utf-8
# Day 03 程序控制语句
# 分段函数求值
x = float(input("input your number"))
result = 0
if x > 1:
    result = 3*x - 5
elif -1 <= x <= 1:
    result = x + 2
else:
    result = 5*x + 3
# Flat is better than nested

# Day 04 循环结构
# range 产生数字序列的函数
c = range(10)
# 猜谜游戏
import random
while True:
    result = random.randrange(0,100)
    while True:
        x = int(input("input your int"))
        if x < result:
            print "bigger"
        elif x > result:
            print "smaller"
        else:
            print "Done"
            break
