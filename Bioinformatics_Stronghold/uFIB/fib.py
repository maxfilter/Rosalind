'''
Rabbits and Recurrence Relations
2019.02.28

Given: Positive integers n<=40 and k<=5.

Return: The total number of rabbit pairs that will be present after n months, if
we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''
import sys

def find_rabbit_pairs(n, k):
    if (n <= 1):
        return k
    else:
        return n + find_rabbit_pairs(n-1, k+n)

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        values = f.read().strip().split()
        n = int(values[0])
        k = int(values[1])

    print(find_rabbit_pairs(n, k))
