#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

eps =  1e-10
EULER = 0.5772156649015328606

if __name__ == "__main__":

    x = float(input("Value of x? "))
    if x == 0:
        print("illegal value of x", file = sys.stderr)
        exit(1)
    a = x
    s, k = a, 1
    while math.fabs(a)> eps:
        a *= x*k/(k+1)**2
        s +=a
        k+= 1
    print(f"Ei({x}) = {EULER + math.log(math.fabs(x))+s}")
