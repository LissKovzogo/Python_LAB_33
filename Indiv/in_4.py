import math
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    x = float(input("Введите x: "))
    eps = 1e-10
    gamma = 0.57721566490153286060

    result_f = gamma + math.log(x)
    n = 1
    a = -(x**2)/4
    result = a
    while abs(a) > eps:
        a *= ((-x**2)*(2*n))/((2*n+2)*(2*n+2)*(2*n+1))
        result += a
        n += 1

    print(f"Ci({x}) = {result_f + result}")
