'''
@title: Transcribing DNA into RNA
@ID: RNA
@date: 2019.02.26
'''

import sys

def main():
    '''
    Transcribes DNA into RNA

    Given: A DNA string t having length at most 1000 nt.
    Return: The transcribed RNA string of t.
    '''
    with open(sys.argv[1],'r') as f:
        sequence = f.read().strip()

    print(sequence.replace('T', 'U'))


if __name__ == '__main__':
    main()
