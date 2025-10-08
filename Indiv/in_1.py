#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    x = int(input("Value of x? "))
    zp = 0
    if x <= 50:
        zp = 30 * x
    elif 50 < x <= 75:
        zp = 50 * x
    elif 75 < x <= 90:
        zp = 65 * x
    else: zp = 70 * x + 2000

    print(f"Заработок в копейках = {zp}, "
          f"Заработок в рублях = {zp/100}")