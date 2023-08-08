#!/usr/bin/python3
for letter_lc in range(97, 123):
    if chr(letter_lc) != 'q' and chr(letter_lc) != 'e':
        print("{}".format(chr(letter_lc)), end="")
