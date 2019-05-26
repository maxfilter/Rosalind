'''
Rabbits and Recurrence Relations
2019.02.28

Given: Positive integers n<=40 and k<=5.

Return: The total number of rabbit pairs that will be present after n months, if
we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Sample Dataset:
    5 3
Sample Output:
    19
'''
import sys

def rabbit_pairs(n, k):
    num_pairs = [0, 1, 1]

    for i in range(3, n + 1):
        num_pairs.append(num_pairs[i - 1] + k*num_pairs[i - 2])

    return num_pairs[n]

def main():
    with open(sys.argv[1], 'r') as f:
        values = f.read().strip().split()
        n = int(values[0]) # number of months
        k = int(values[1]) # number of pairs of rabbits per litter

    with open('output.txt', 'w') as output:
        output.write(str(rabbit_pairs(n, k)))

if __name__ == "__main__":
    main()
