#!/usr/bin/python3
import sys

i = len(sys.argv) - 1

if i == 0:
    print("0 arguments.")
elif i == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(i))
for j in range(len(sys.argv) - 1):
    print("{}: {}".format(j + 1, sys.argv[j + 1]))