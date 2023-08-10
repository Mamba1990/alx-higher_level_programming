#!/usr/bin/python3

if __name__ == "__main__":
    """Display the sum of all arguments."""
    import sys

    add = 0
    for j in range(len(sys.argv) - 1):
    add += int(sys.argv[j + 1])
    print("{}".format(t))
