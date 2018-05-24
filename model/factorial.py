#!/usr/bin/env python3
'''
A simple factorial function embedded in a dev ecosystem with travis
'''

def factorial(number):
    '''
    recursive function that return the factorial of an int
    '''
    assert isinstance(number, int)
    if number == 0:
        return 1
    return factorial(number-1)*number


if __name__ == '__main__':
    import sys
    def usage():
        '''usage of the command line'''
        text = '''usage : python3 {} n
with n being an integer
        '''.format(sys.argv[0])
        print(text)

    if len(sys.argv) > 1:
        try:
            NUM = int(sys.argv[1])
            print(factorial(NUM))
        except ValueError:
            usage()
            sys.exit(1)
    else:
        usage()
