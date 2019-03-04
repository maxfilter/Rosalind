'''
Finding a Motif in DNA
2019.02.28

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
'''
import sys

def find_motif(sequence, motif):
    locations = ''

    for i in range(0, len(sequence)-len(motif)+1, 1):
        if motif == sequence[i:i+len(motif)]:
            locations += str(i+1) + ' '

    return locations.rstrip()

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()

    print(find_motif(s, t))
