## Find given interger and determine
## if it is a prime number

import sys


def is_prime(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def main(args):
    for s in args:
        print(s, is_prime(int(s)))


if __name__ == '__main__':
    main(sys.argv[1:])
