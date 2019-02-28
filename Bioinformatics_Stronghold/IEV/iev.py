'''
Calculating Expected Offspring
2019.02.27

Given: Six nonnegative integers, each of which does not exceed 20,000.
The integers correspond to the number of couples in a population possessing each
genotype pairing for a given factor. In order, the six given integers represent
the number of couples having the following genotypes:

    1. AA-AA
    2. AA-Aa
    3. AA-aa
    4. Aa-Aa
    5. Aa-aa
    6. aa-aa

Return: The expected number of offspring displaying the dominant phenotype in
the next generation, under the assumption that every couple has exactly two
offspring
'''
import sys

with open(sys.argv[1], 'r') as f:
    genotype_pairings = f.read().split()

# probability dominant
p_dominant = [1, 1, 1, 0.75, 0.5, 0]
expected = 0

for gp, prob in zip(genotype_pairings, p_dominant):
    expected += int(gp)*prob

print(2*expected) # each couple has 2 offspring
