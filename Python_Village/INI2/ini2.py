'''
Variables and Some Arithmetic

Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right
    triangle whose legs have lengths a and b.
'''
import sys

def get_hypotenuse_square(a, b):
    return a**2 + b**2

def main():
    with open(sys.argv[1], 'r') as f:
        a, b = f.read().split()

    print(get_hypotenuse_square(int(a), int(b)))

if __name__ == '__main__':
    main()
