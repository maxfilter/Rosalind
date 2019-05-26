'''
Enumerating Oriented Gene Orderings

Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list
of all such permutations (you may list the signed permutations in any order).
'''
import sys
import itertools

def get_signed_permutation_sequence(n):
    '''
    Returns a list with the positive and negative values of the digit n,
    excluding 0
    '''
    permutation_sequence = []
    for i in range(-n, n+1):
        if (i != 0):
            permutation_sequence.append(i)

    return permutation_sequence

def generate_signed_permutations_of(n):
    permutation_sequence = get_signed_permutation_sequence(n)
    permutations = list(itertools.permutations(permutation_sequence, n))

    # store repeated values in seperate list
    repeated_values = []
    for i, permutation in enumerate(permutations):
        for digit in permutation:
            if ((digit < 0) and (abs(digit) in permutation)):
                repeated_values.append(permutation)

    # remove all repeated values from permutations (ie [-2, ..., 2])
    permutations = set(permutations) - set(repeated_values)

    # make string of permutations
    permutation_string = ''
    for permutation in permutations:
        for digit in permutation:
            permutation_string += str(digit) + ' '
        permutation_string += '\n'
    return permutation_string

def main():
    with open(sys.argv[1], 'r') as f:
        n = int(f.read().strip())

    signed_permutations = generate_signed_permutations_of(n)
    num_elements = signed_permutations.count('\n')

    with open("output.txt", 'w') as output:
        output.write(str(num_elements)+'\n')
        output.write(signed_permutations)

if __name__ == "__main__":
    main()
