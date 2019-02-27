'''
@title: Counting DNA Nucleotides
@ID: DNA
@date: 2019.02.26
'''
import sys

def main():
    '''
    Analyzes a DNA sequence and counts the nucleotides of each base.

    Given: A DNA string 's' of length at most 1000 nucleotides
    Return: Four integers (separated by spaces) counting the respective number
            of time that the symbols 'A', 'C', 'G', and 'T' occur in s.
    '''
    with open(sys.argv[1], 'r') as f:
        s = f.read().strip();

    for nt in 'ACGT':
        print s.count(nt),


if __name__ == '__main__':
    main()
