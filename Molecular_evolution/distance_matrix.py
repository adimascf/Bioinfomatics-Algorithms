
from os import read


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


def hamming_distance(seq1, seq2):
    """return number of difference char fro two same length string"""
    result = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            result += 1
    return result


def distance_matrix(list_seq):
    """Creates distance matrix from given a list of seqeunces"""

    matrix = [[0 for _ in range(len(list_seq))] for _ in range(len(list_seq))]
    k = len(list_seq[0])
    for i in range(len(list_seq)):
        for j in range(len(list_seq)):
            matrix[i][j] = format(hamming_distance(
                list_seq[i], list_seq[j])/k, '.5f')
    return matrix


# list_seq_test = list(read_fasta('E:rosalind/rosalind_pdst.txt').values())
# matrix = distance_matrix(list_seq_test)
# for row in matrix:
#     print(*row)
