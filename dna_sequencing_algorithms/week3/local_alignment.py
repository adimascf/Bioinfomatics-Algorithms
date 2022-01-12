from collections import defaultdict


def scroing_matrix(a, b):

    bases = ['A', 'T', 'C', 'G']
    matrix = defaultdict(dict)
    for base1 in bases:
        for base2 in bases:
            if base1 == base2:
                matrix[base1+base2] = 2
            else:
                matrix[base1+base2] = -4
    return matrix[a+b]


def local_alignment(seq1, seq2, indels=-6):
    """Look elements in the matrix that has maximum value.
    Traceback from there until reach element that has zero value"""

    k1, k2 = len(seq1), len(seq2)
    s = [[0 for _ in range(k2+1)] for _ in range(k1+1)]
    for i in range(k1+1):
        s[i][0] = 0
    for i in range(k2+1):
        s[0][i] = 0

    i_idx, j_idx = 0, 0
    for i in range(1, k1+1):
        for j in range(1, k2+1):
            delta = scroing_matrix(seq1[i-1], seq2[j-1])
            s[i][j] = max(s[i-1][j-1] + delta, s[i-1][j] + indels,
                          s[i][j-1] + indels, 0)

            if s[i][j] > s[i_idx][j_idx]:
                i_idx, j_idx = i, j
    return s, i_idx, j_idx


x, y = 'GGTATGCTGGCGCTA', 'TATATGCGGCGTTT'
matrix, i, j = local_alignment(x, y)
print(matrix[i][j])
