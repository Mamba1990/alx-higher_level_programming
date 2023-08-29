#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0
    for k in range(1, 3):
        try:
            if k > a:
                raise Exception('Too far')
            r += a ** b / k
        except Exception:
            r = b + a
            break
    return r
