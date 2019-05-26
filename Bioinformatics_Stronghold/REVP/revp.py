import sys
from typing import NamedTuple

complements = {
    'A' : 'T',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C',
}

class DNA(NamedTuple):
    name: str
    sequence: str

def reverse_complement(str):
    rev_c = ''

    # get complement of sub string
    for bp in str:
        rev_c += complements[bp]

    # return reverse of complement
    return rev_c[::-1]

def reverse_palindromes(dna):
    sequence = dna.sequence

    rev_ps = ''

    for pos in range(len(sequence)):
        for length in range(4, 13):

            if (pos + length > len(sequence)):
                continue

            sub_seq = sequence[pos : pos + length]

            if ((len(sub_seq) >= 4) and sub_seq == reverse_complement(sub_seq)):
                rev_ps += str(pos + 1) + ' ' + str(length) + '\n'

    return rev_ps


def parse_fasta():
    DNA_list = []

    # read specified input file and store each FASTA sequence into a dna object
    with open(sys.argv[1], 'r') as f:

        # splits file into a list of fasta sequences
        buf = f.read().split('>')[1:]

        # creates a formatted dna object from each dna string and adds it to a list
        for dna_str in buf:
            dna_str = dna_str.split('\n')

            name = dna_str[0]
            sequence = ''

            for line in dna_str[1:]:
                sequence += line

            dna = DNA(name, sequence)
            DNA_list.append(dna)

    return DNA_list

def main():
    dna_list = parse_fasta()

    rev_ps = reverse_palindromes(dna_list[0])

    with open("output.txt", 'w') as output:
        output.write(rev_ps)


if __name__ == "__main__":
    main()
