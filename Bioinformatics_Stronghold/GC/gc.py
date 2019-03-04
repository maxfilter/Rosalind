'''
Calculating GC content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error
below.
'''
import sys

def compute_gc_content(sequence):
    num_GC = float(sequence.count("G") + sequence.count("C"))
    num_bases = float(num_GC + sequence.count("A") + sequence.count("T"))

    return 100*num_GC/num_bases

def main():
    '''
    Reads DNA strings from a txt file in FASTA format and prints the ID and
    string corresponding to the largest gc-content
    '''
    with open(sys.argv[1], 'r') as f:
        DNA_strings = f.read().strip().split(">")[1:] # ignore before first >

    max_gc_content = 0.0
    max_gc_fasta = ''

    for string in DNA_strings:
        string = string.strip()

        id, sequence = string.split("\n", 1)

        gc_content = compute_gc_content(sequence)

        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_fasta = id + '\n' + str(max_gc_content)

    print(max_gc_fasta)

if __name__ == "__main__":
    main()
