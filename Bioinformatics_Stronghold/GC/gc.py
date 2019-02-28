'''
Calculating GC content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error
below.
'''
import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        fasta = f.read()

    for line in fasta:
        print(line)
