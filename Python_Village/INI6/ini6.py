'''
Dictionaries

Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated
by spaces. Words are case-sensitive, and the lines in the output can be in any order.
'''
import sys
import pprint

def get_word_occurrences(str):
    WORD_OCCURRENCES = {}
    list_words = str.split()

    for word in list_words:
        if word not in WORD_OCCURRENCES:
            WORD_OCCURRENCES[word] = 1
        else:
            WORD_OCCURRENCES[word] += 1

    return WORD_OCCURRENCES

def print_word_occurrences(dict):
    for item in dict:
        print(item, ' ', dict[item])

def main():
    with open(sys.argv[1], 'r') as f:
        str = f.read().strip()

    word_occurrences = get_word_occurrences(str)
    print_word_occurrences(word_occurrences)

if __name__ == "__main__":
    main()
