#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    if arg <= 1:
        print("{} arguments.".format(arg - 1))
    elif arg == 2:
        print("{} argument:".format(arg - 1))
    else:
        print("{} arguments:".format(arg - 1))
    for a in range(1, arg):
        print("{}: {}".format(a, sys.argv[a]))
