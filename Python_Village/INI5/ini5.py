'''
Working with Files

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file.
Assume 1-based numbering of lines.
'''
import sys

def main():
    output_lines = []

    with open(sys.argv[1], 'r') as input:
        i = 1
        for line in input:
            if (i % 2 == 0):
                output_lines.append(line)
            i += 1

    with open("output.txt", 'w') as out:
        for line in output_lines:
            out.write(line)

if __name__ == "__main__":
    main()
