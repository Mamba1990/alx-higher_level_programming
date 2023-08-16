#!/usr/bin/python3
def to_subtract(list_num):
    toSub = 0
    maxList = max(list_num)

    for m in list_num:
        if maxList > m:
            toSub += m

    return (maxList - toSub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    romN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listKeys = list(romN.keys())

    _num = 0
    lastRom = 0
    list_num = [0]

    for c in roman_string:
        for rNum in listKeys:
            if rNum == c:
                if romN.get(c) <= lastRom:
                    _num += to_subtract(list_num)
                    list_num = [romN.get(c)]
                else:
                    list_num.append(romN.get(c))

                lastRom = romN.get(c)

    _num += to_subtract(list_num)

    return (_num)
