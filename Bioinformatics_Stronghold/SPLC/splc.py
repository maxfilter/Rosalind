'''
Given:
    A DNA string s (of length at most 1 kbp) and a collection of substrings
    of s acting as introns. All strings are given in FASTA format.

Return:
    A protein string resulting from transcribing and translating the exons
    of s. (Note: Only one solution will exist for the dataset provided.)
'''
import sys
from typing import NamedTuple

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

def transcribe_sequence(sequence, introns):
    
    for intron in introns:
        sequence = sequence.replace(intron, '')

    return sequence

def translate_sequence(sequence):
    translated_sequence = ''

    for i in range(0, len(sequence), 3):
        codon = sequence[i: i + 3]
        if (DNA_CODON_TABLE[codon] == 'Stop'):
            break
        else:
            translated_sequence += DNA_CODON_TABLE[codon]

    return translated_sequence

def main():
    DNA_list = []

    # read specified input file and store each FASTA sequence into a dna object
    with open(sys.argv[1], 'r') as f:
        DNA_list = read_fasta(f)

    DNA_sequences = dna_strings(DNA_list)
    sequence = DNA_sequences[0]
    introns = DNA_sequences[1:]

    transcribed_sequence = transcribe_sequence(sequence, introns)

    translated_sequence = translate_sequence(transcribed_sequence)

    # writes the solution to a text file
    with open("output.txt", 'w') as output:
        output.write(translated_sequence)

if __name__ == "__main__":
    main()
