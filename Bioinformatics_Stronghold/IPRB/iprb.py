'''
Mendel's First Law
2019.02.27

Given:  Three positive integers k, m, and n, representing a population
        containing k+m+n organisms: k individuals are homozygous dominant for a
        factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce
        an individual possessing a dominant allele (and thus displaying the
        dominant phenotype). Assume that any two organisms can mate.
'''
import sys

with open(sys.argv[1], 'r') as f:
    population = f.read().strip().split()

k = float(population[0])
m = float(population[1])
n = float(population[2])

pop_size = k+m+n #total organisms in population
p_dominant = 0

# dominant-dominant 100%
p_dominant += (k/pop_size)*((k-1)/(pop_size-1))
# dominant-heterozygous 100%
p_dominant += 2*(k/pop_size)*(m/(pop_size-1))
# dominant-recessive 100%
p_dominant += 2*(k/pop_size)*(n/(pop_size-1))
# heterozygous-heterozygous - 75% chance of showing dominant trait
p_dominant += (m/pop_size)*((m-1)/(pop_size-1))*0.75
# heterozygous-recessive - 50% chance of showing dominant trait
p_dominant += 2*(m/pop_size)*(n/(pop_size-1))*0.5

print(p_dominant)
