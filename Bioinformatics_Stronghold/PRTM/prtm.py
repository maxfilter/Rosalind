'''
Calculating Protein Mass
2019.02.27

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
'''
import sys

MONOISOTOPIC_MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}

def calculate_weight(protein_string):
    weight = 0

    for protein in protein_string:
        weight += MONOISOTOPIC_MASS_TABLE[protein]

    return weight

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        protein_string = f.read().strip()

    print(calculate_weight(protein_string))
