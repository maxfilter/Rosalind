'''
Counting Point Mutations
2019.02.27

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
'''
import sys

with open(sys.argv[1], 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()

d_hamm = 0

for b1, b2 in zip(s, t):
    if (b1 != b2):
        d_hamm += 1

print(d_hamm)
