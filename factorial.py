#!/usr/bin/env python3

def factorial(n):
    assert isinstance(n, int)
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n


if __name__ == '__main__':
    import sys
    def usage():
        usage = '''usage : python3 {} n
with n being an integer
        '''.format(sys.argv[0])
        print(usage)

    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            print(factorial(n))
        except ValueError:
            usage()
            sys.exit(1)
    else:
        usage()
