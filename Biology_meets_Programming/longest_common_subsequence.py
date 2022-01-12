from typing import Match


def read_fasta(file_path):
    '''Reading fasta formatted file and returning into line'''
    with open(file_path, 'r') as f:
        # for storing the contents of the file into a list
        fasta_file = [line.strip('\n') for line in f.readlines()]

    # for storing labels and data
    fasta_dict = {}
    fasta_label = ''

    # for preparing data and taking into dictionary
    for line in fasta_file:
        if '>' in line:
            fasta_label = line
            fasta_dict[fasta_label] = ''
        else:
            fasta_dict[fasta_label] += line
    return fasta_dict


def manhattan_grid(seq1, seq2):
    """Creates manhatan grid and saved which edge to s(i,j) to the backtrack matrix"""

    s = [[0 for _ in range(len(seq2) + 1)] for _ in range(len(seq1) + 1)]
    backtrace = [[0 for _ in range(len(seq2))] for _ in range(len(seq1))]

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            match = 0
            if seq1[i - 1] == seq2[j - 1]:
                match = 1
            s[i][j] = max(s[i][j - 1], s[i - 1][j], s[i - 1][j - 1] + match)

            if s[i][j] == s[i][j - 1]:
                backtrace[i - 1][j - 1] = 'east'
            elif s[i][j] == s[i - 1][j]:
                backtrace[i - 1][j - 1] = 'south'
            elif s[i][j] == s[i - 1][j - 1] + match:
                backtrace[i - 1][j - 1] = 'southeast'

    return backtrace


def backtracing(backtrace, seq1, seq2):
    """Finding longest common subsequence with bractracking that all
    edges recorded"""

    lcs = ''
    i = len(seq1)
    j = len(seq2)
    while i > 0 and j > 0:
        if backtrace[i - 1][j - 1] == 'southeast':
            lcs += seq1[i - 1]
            i -= 1
            j -= 1
        elif backtrace[i - 1][j - 1] == 'south':
            i -= 1
        else:
            j -= 1
    return lcs[::-1]


seqs = read_fasta('E:rosalind/rosalind_lcsq.txt')
seq1_test, seq2_test = seqs.values()
backtrace = manhattan_grid(seq1_test, seq2_test)
print(backtracing(backtrace, seq1_test, seq2_test))