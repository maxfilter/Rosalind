'''
Enumerating Gene Orders
03.02.2019

Given: A positive integer n<=7.

Return: The total number of permutations of length n, followed by a list of all
such permutations (in any order).
'''

import sys
import itertools

def get_permutation_sequence(n):
    permutation_sequence = []
    for i in range(n):
        permutation_sequence.append(i+1)

    return permutation_sequence

def get_num_permutations(n):
    permutations = 1
    for i in range(1, n+1):
        permutations *= i

    return permutations

def generate_permutations_of(n):
    permutation_sequence = get_permutation_sequence(n) # [1, 2, 3] for 3
    permutations = list(itertools.permutations(permutation_sequence))
    permutation_string = ''
    for permutation in permutations:
        for digit in permutation:
            permutation_string += str(digit) + ' '
        permutation_string += '\n'
    return permutation_string

def main():
    with open(sys.argv[1], 'r') as f:
        n = int(f.read().strip())

    print(get_num_permutations(n))
    print(generate_permutations_of(n))

if __name__ == "__main__":
    main()
