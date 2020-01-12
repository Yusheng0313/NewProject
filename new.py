# ！/usr/bin/env python
# -*- coding:utf-8 -*-

# str = 'Hello World!'
# print(str)

import turtle
import math

t = turtle.Turtle()

for i in range(1):
    t.forward(i * 5)
    t.right(144)

sum = 0
for i in range(1, 100):
    sum = sum + i*((-1)**(i+1))
print(sum)


while True:
    num5 = float(input("please input the num:"))
    a = num5 % 10
    b = (num5 - a) / 10 % 10
    c = (num5 - b*10 - a) / 100 % 10
    d = (num5 - c*100 - b*10 - a) / 1000 % 10
    e = (num5 - d*1000 - c*100 - b*10 - a) / 10000 % 10
    if a == e and b == d and 100000 > num5 > 10000:
        print(a, b, c, d, e)
        break

x = 1
while 0 < x < 100:

    if float(math.sqrt(x+100)).is_integer() and float(math.sqrt(x+100+168)).is_integer():
        print('result：', x)
        break

    x = x + 1

# 1! + 2! + 3! + … + 20! = 2561327494111820313
x = 1
sum = 0
while x < 21:
    acc = 1
    for i in range(1, x+1):
        acc = acc * i
    sum = sum + acc
    x = x + 1

print('result:', x,  acc, sum)





