import math
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    x = float(input("Введите x: "))
    epsilon = 1e-10
    gamma = 0.57721566490153286060

    result = gamma + math.log(x)
    n = 1
    term = 1

    while abs(term) > epsilon:
        term = ((-1) ** n) * (x ** (2 * n)) / (2 * n * math.factorial(2 * n))
        result += term
        n += 1

    print(f"Ci({x}) = {result}")