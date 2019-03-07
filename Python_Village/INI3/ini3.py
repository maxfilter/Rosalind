'''
Strings and Lists

Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with
space in between), inclusively. In other words, we should include elements s[b]
and s[d] in our slice.
'''
import sys

def main():
    with open(sys.argv[1], 'r') as f:
        str = f.readline().strip()
        a, b, c, d = f.readline().split()

        str_a = str[int(a):int(b)+1]
        str_b = str[int(c):int(d)+1]

        output = str_a + ' ' + str_b
        print(output)

if __name__ == "__main__":
    main()
