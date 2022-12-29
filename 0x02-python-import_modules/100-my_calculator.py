#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import exit, argv

    signs = {'+': add, '-': sub, '*': mul, '/': div}

    if len(argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in signs:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    c = argv[2]
    d = signs[c](a, b)
    print("{} {} {} = {}".format(a, c, b, d))
