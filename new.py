# ！/usr/bin/env python
# -*- coding:utf-8 -*-

# str = 'Hello World!'
# print(str)

import turtle

t = turtle.Turtle()

for i in range(10):
    t.forward(i * 5)
    t.right(144)

sum = 0
for i in range(1,100):
    sum = sum + i*((-1)**(i+1))
print(sum)


while True :
    num5 = float(input("please input the num:"))
    a = num5 % 10
    b = (num5 - a) / 10 % 10
    c = (num5 - b*10 - a) / 100 % 10
    d = (num5 - c*100 - b*10 - a) / 1000 % 10
    e = (num5 - d*1000 - c*100 - b*10 - a) / 10000 % 10
    if a == e and b == d and 100000 > num5 > 10000:
        print(a, b, c, d, e)
        break





