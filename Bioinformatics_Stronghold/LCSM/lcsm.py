'''
Finding a Shared Motif

Given:
    A collection of k (k≤100) DNA strings of length at most 1 kbp each in
    FASTA format.

Return:
    A longest common substring of the collection. (If multiple solutions exist,
    you may return any single solution.)

Sample Dataset:
    >Rosalind_1
    GATTACA
    >Rosalind_2
    TAGACCA
    >Rosalind_3
    ATACA

Sample Output:
    AC
'''
import sys
from typing import NamedTuple

class DNA(NamedTuple):
    name: str
    sequence: str

def read_fasta(fp):
    DNA_list = []

    # splits file into a list of fasta sequences
    buff = fp.read().split('>')[1:]
    # creates a formatted dna object from each dna string and adds it to a list
    for dna_fasta in buff:
        dna_fasta = dna_fasta.split('\n')

        name = dna_fasta[0]
        sequence = ''

        for line in dna_fasta[1:]:
            sequence += line

        dna = DNA(name, sequence)
        DNA_list.append(dna)

    return DNA_list

def dna_strings(DNA_list):
    DNA_strings = []

    for dna in DNA_list:
        DNA_strings.append(dna.sequence)

    # returns a list of DNA strings
    return DNA_strings

def lcs(DNA_sequences):
    shortest_seq = min(DNA_sequences, key=len)

    lcs = ''

    for i in range(len(shortest_seq)):
        for j in range(i, len(shortest_seq)):
            substring = shortest_seq[i: j + 1]

            contained = True
            for seq in DNA_sequences:
                if (contained):
                    if (substring not in seq):
                        contained = False

            if (contained and (len(substring) >= len(lcs))):
                lcs = substring

    return lcs


def main():
    DNA_list = []

    # read specified input file and store each FASTA sequence into a dna object
    with open(sys.argv[1], 'r') as f:
        DNA_list = read_fasta(f)

    DNA_sequences = dna_strings(DNA_list)

    longest_common_substring = lcs(DNA_sequences)

    # writes the solution to a text file
    with open("output.txt", 'w') as output:
        output.write(longest_common_substring)


if __name__ == "__main__":
    main()
