'''
Complementing a Strand of DNA

Given: A DNA string s of length at most 1000 base pairs
Returns: The reverse complement s^c of s
'''
import sys

conjugate = {
    'A' : 'T',
    'C' : 'G',
    'G' : 'C',
    'T' : 'A',
}

with open(sys.argv[1], 'r') as f:
    s = f.read().strip()

sequence = s[::-1] #reverse the string and break it into a list
conjugate_string = ''

for base_pair in sequence:
    conjugate_string += conjugate[base_pair]

print(conjugate_string)
