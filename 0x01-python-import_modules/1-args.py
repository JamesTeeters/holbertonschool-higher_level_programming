#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    if num == 0:
        print("0 arguments.")
        exit()
    if num == 1:
        arg = 'argument'
    else:
        arg = 'arguments'
    print("{} {}:".format(num, arg))
    c = 1
    for i in argv[1:]:
        print("{}: {}".format(c, argv[c]))
        c += 1
