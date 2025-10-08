#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    x = int(input("Value of x? "))
    y = int(input("Value of y? "))

    if x % y == 0:
        print("x делится на у без остатка")
    else:
        print("x не делится на у без остатка")