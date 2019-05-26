'''
Consensus and Profile

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in
    FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
    possible consensus strings exist, then you may return any one of them.)
'''
import sys
from typing import NamedTuple
from numpy import zeros

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

def profile_arr(DNA_strings):
    profile = zeros([4, len(DNA_strings[0])])

    for sequence in DNA_strings:
        for i in range(len(sequence)):
            bp = sequence[i]

            if (bp == 'A'):
                profile[0][i] += 1
            elif (bp == 'C'):
                profile[1][i] += 1
            elif (bp == 'G'):
                profile[2][i] += 1
            elif (bp == 'T'):
                profile[3][i] += 1

    return profile

def profile_str(profile):
    profile_str = ''

    # don't know how to use enumerated types in python
    for i in range(len(profile)):
        if (i == 0):
            profile_str += 'A:'
        elif (i == 1):
            profile_str += 'C:'
        elif (i == 2):
            profile_str += 'G:'
        elif (i == 3):
            profile_str += 'T:'

        for j in range(len(profile[i])):
            profile_str += ' ' + str(int(profile[i][j]))

        profile_str += '\n'

    return profile_str

def consensus(profile):
    consensus_str = ''

    for i in range(len(profile[0])):
        maximum = max(profile[0][i], profile[1][i], profile[2][i], profile[3][i])

        if (maximum == profile[0][i]):
            consensus_str += 'A'
        elif (maximum == profile[1][i]):
            consensus_str += 'C'
        elif (maximum == profile[2][i]):
            consensus_str += 'G'
        elif (maximum == profile[3][i]):
            consensus_str += 'T'

    consensus_str += '\n'
    return consensus_str

def main():
    DNA_list = []

    # read specified input file and store each FASTA sequence into a dna object
    with open(sys.argv[1], 'r') as f:
        DNA_list = read_fasta(f)

    DNA_strings = dna_strings(DNA_list)

    profile = []
    profile_s = ''

    profile = profile_arr(DNA_strings)

    consensus_s = consensus(profile)
    profile_s = profile_str(profile)

    # writes the solution to a text file
    with open("output.txt", 'w') as output:
        output.write(consensus_s)
        output.write(profile_s)

if __name__ == "__main__":
    main()
