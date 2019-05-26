'''
Partial Permutations

Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.
'''

import sys

def get_partial_permutations(n, k):
    partial_permutations = 1
    for i in range(k):
        partial_permutations *= (n-i)
        partial_permutations %= 1000000

    return partial_permutations

def main():
    with open(sys.argv[1], 'r') as f:
        n, k = f.read().strip().split()

    print(get_partial_permutations(int(n), int(k)))

if __name__ == "__main__":
    main()
