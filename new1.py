# ！/usr/bin/env python
# -*- coding:utf-8 -*-


n = 100
while n <= 999:
    ans = n

    n0 = ans % 10
    ans = (ans - n0) / 10
    n1 = ans % 10
    ans = (ans - n1) / 10
    n2 = ans

    if n0 ** 3 + n1 ** 3 + n2 ** 3 == n:
        print(n)


    n += 1

