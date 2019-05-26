import sys

def rabbit_pairs(n, m):
    num_pairs = [1]

    for i in range(n - 1):
        num_pairs.append(sum(num_pairs[0:-1]))

        if (i + 1 >= m):
            del num_pairs[0]

    return sum(num_pairs)

def main():
    with open(sys.argv[1], 'r') as f:
        values = f.read().strip().split()
        n = int(values[0]) # number of months
        m = int(values[1]) # rabbit life span

    with open('output.txt', 'w') as output:
        output.write(str(rabbit_pairs(n, m)))

if __name__ == "__main__":
    main()
