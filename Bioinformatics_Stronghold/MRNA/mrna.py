'''
Inferring mRNA from Protein

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could
have been translated, modulo 1,000,000. (Don't neglect the importance of the
stop codon in protein translation.)
'''
import sys

NUM_CODONS_FOR_AA = {
    'A': 4,
    'C': 2,
    'D': 2,
    'E': 2,
    'F': 2,
    'G': 4,
    'H': 2,
    'I': 3,
    'K': 2,
    'L': 6,
    'M': 1,
    'N': 2,
    'P': 4,
    'Q': 2,
    'R': 6,
    'S': 6,
    'T': 4,
    'V': 4,
    'W': 1,
    'Y': 2,
    'Stop': 3,
}

def get_num_rna_strings(protein_string):
    '''
    For a given protein string, returns the total number of possible rna strings
    from which the protein could have been derived, modulo 1000000, including the
    stop codons
    '''
    rna_strings = 1 # num possible rna strings

    for protein in protein_string:
        rna_strings *= NUM_CODONS_FOR_AA[protein]
        rna_strings %= 1000000
    rna_strings *= NUM_CODONS_FOR_AA['Stop']
    rna_strings %= 1000000

    return rna_strings

def main():
    with open(sys.argv[1], 'r') as f:
        protein_lines = [line.strip() for line in f.read()]
    protein_string = "".join(protein_lines)

    print(get_num_rna_strings(protein_string))


if __name__ == "__main__":
    main()
