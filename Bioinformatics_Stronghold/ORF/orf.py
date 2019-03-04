'''
Open Reading Frames
2019.03.01

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs
of s. Strings can be returned in any order.
'''
import sys

CONJUGATE = {
    'A' : 'T',
    'C' : 'G',
    'G' : 'C',
    'T' : 'A',
}

DNA_CODON_TABLE = {
    'TTT': 'F',      'CTT': 'L',      'ATT': 'I',      'GTT': 'V',
    'TTC': 'F',      'CTC': 'L',      'ATC': 'I',      'GTC': 'V',
    'TTA': 'L',      'CTA': 'L',      'ATA': 'I',      'GTA': 'V',
    'TTG': 'L',      'CTG': 'L',      'ATG': 'M',      'GTG': 'V',
    'TCT': 'S',      'CCT': 'P',      'ACT': 'T',      'GCT': 'A',
    'TCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    'TCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    'TCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    'TAT': 'Y',      'CAT': 'H',      'AAT': 'N',      'GAT': 'D',
    'TAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    'TAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    'TAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    'TGT': 'C',      'CGT': 'R',      'AGT': 'S',      'GGT': 'G',
    'TGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    'TGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    'TGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G',
}

def translate_codon(codon):
    '''
    Translates codon into an amino acid
    '''
    protein = None
    if len(codon) == 3 and codon in DNA_CODON_TABLE:
        protein = DNA_CODON_TABLE[codon]

    return protein

def get_reverse_complement(dna):
    sequence = dna[::-1] #reverse the string and break it into a list
    reverse_complement = ''

    for base_pair in sequence:
        reverse_complement += CONJUGATE[base_pair]

    return reverse_complement

def find_protein_strings(dna):
    protein_strings = []

    # Find the index locations of each start codon at any point in the list
    start_locations = []

    for i in range(len(dna)):
        codon = dna[i:i+3]
        if codon == 'ATG':
            start_locations.append(i)

    # Start at each of those index locations and identify possible proteins
    for start_location in start_locations:
        protein = ''
        found_stop = False

        for i in range(start_location, len(dna), 3):
            codon = dna[i:i+3]
            amino_acid = translate_codon(codon)

            if not amino_acid:
                break
            if amino_acid == 'Stop':
                found_stop = True
                break
            else:
                protein += amino_acid

        if found_stop:
            protein_strings.append(protein)

    return protein_strings

def main():
    with open(sys.argv[1], 'r') as f:
        dna = f.read().strip().split('\n')[1:]

    for line in dna:
        line = line.strip()

    dna = ''.join(dna) # make dna one continuous string w no newlines

    rc_dna = get_reverse_complement(dna)

    dna_proteins = find_protein_strings(dna)
    rc_dna_proteins = find_protein_strings(rc_dna)

    print('\n'.join(set(dna_proteins + rc_dna_proteins)))

if __name__ == "__main__":
    main()
