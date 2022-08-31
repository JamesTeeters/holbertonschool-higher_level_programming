#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    if num == 0:
        punc = '.'
    else:
        punc = ':'
    if num == 1:
        arg = "argument"
    else:
        arg = "arguments"
    
    i = 1
    print("{} {}{}".format(num, arg, punc))
    for i in argv[1:]:
        print ("{}: {}".foramt(count, argv[i]))
        i += 1 
