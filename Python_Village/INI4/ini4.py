'''
Conditions and Loops

Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
'''
import sys

def sum_odd(a, b):
    sum = 0
    for digit in range(a, b):
        if (digit % 2 == 1):
            sum += digit

    return sum

def main():
    with open(sys.argv[1], 'r') as f:
        a, b = f.read().split()

        print(sum_odd(int(a), int(b)))

if __name__ == "__main__":
    main()
