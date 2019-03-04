'''
NOT FUNCTIONAL

Enumerating Gene Orders
03.02.2019

Given: A positive integer n<=7.

Return: The total number of permutations of length n, followed by a list of all
such permutations (in any order).
'''

import sys

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

def print_permutations_of(p_seq):
    if (len(p_seq) == 1):
        print(str(p_seq[0]))
    else:
        for i in range(len(p_seq)):
            next_seq = [p_seq[n] for n in range(len(p_seq)) if p_seq[n] != p_seq[i]]

            for j in range(1, int(get_num_permutations(len(p_seq))/len(p_seq))+1):
                print(str(i+1), end='')
                print(next_seq)
                #print_permutations_of(next_seq)

def main():
    with open(sys.argv[1], 'r') as f:
        n = int(f.read().strip())

    permutation_sequence = get_permutation_sequence(n)
    print_permutations_of([1,2,3])
    # print_permutations_of(permutation_sequence)

    # print('\n'.join(permutations))

if __name__ == "__main__":
    main()
