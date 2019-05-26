'''
Overlap Graphs

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

Sample Dataset:
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output:
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
'''
import sys
from typing import NamedTuple

class DNA(NamedTuple):
    name: str
    sequence: str

def get_adjacency_list(DNA_list, k):
    adjacency_list = []

    for s in DNA_list:
        for t in DNA_list:

            if (s != t): # to prevent directed loops in the overlap graph
                s_suffix = s.sequence[-k:]
                t_prefix = t.sequence[:k]

                if (s_suffix == t_prefix):
                    adjacency = s.name + ' ' + t.name
                    adjacency_list.append(adjacency)

    return adjacency_list

def main():
    DNA_list = []
    k = 3 # substring length

    # read specified input file and store each FASTA sequence into a dna object
    with open(sys.argv[1], 'r') as f:

        # splits file into a list of fasta sequences
        dna_strings = f.read().split('>')[1:]

        # creates a formatted dna object from each dna string and adds it to a list
        for dna_str in dna_strings:
            dna_str = dna_str.split('\n')

            name = dna_str[0]
            sequence = ''

            for line in dna_str[1:]:
                sequence += line

            dna = DNA(name, sequence)
            DNA_list.append(dna)

    adjacency_list = get_adjacency_list(DNA_list, k)

    # writes the solution to a text file
    with open("output.txt", 'w') as output:
        for adjacency in adjacency_list:
            output.write(adjacency + '\n')

if __name__ == '__main__':
    main()
