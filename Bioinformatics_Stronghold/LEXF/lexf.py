'''
Enumerating k-mers Lexicographically

Given: A collection of at most 10 symbols defining an ordered alphabet, and a
positive integer n (n<=10).

Return: All strings of length n that can be formed from the alphabet, ordered
lexicographically (use the standard order of symbols in the English alphabet).
'''
import sys
from itertools import product

def get_ordered_permutations(alphabet, n):
    permutations_list = list(product(alphabet, repeat=n))
    ordered_permutations = ''

    for permutation in permutations_list:
        for base in permutation:
            ordered_permutations += base
        ordered_permutations += '\n'
    return ordered_permutations

def main():
    with open(sys.argv[1], 'r') as f:
        alphabet = f.readline().strip().split()
        n = f.readline().strip() # end string length

    permutations = get_ordered_permutations(alphabet, int(n))

    with open("output.txt", 'w') as f:
        f.write(permutations)

if __name__ == "__main__":
    main()
