from collections import defaultdict


def penalty_matrix(a, b):
    bases = ['A', 'T', 'C', 'G']
    purines = ['A', 'G']
    pirimidines = ['C', 'T']
    matrix = defaultdict(dict)
    for base1 in bases:
        for base2 in bases:
            if base1 == base2:
                matrix[base1+base2] = 0
            elif (base1 in purines and base2 in purines) or (base1 in pirimidines and base2 in pirimidines):
                matrix[base1+base2] = 2
            else:
                matrix[base1+base2] = 4
    return matrix[a+b]


def global_alignment(seq1, seq2, indels=8):

    k1, k2 = len(seq1), len(seq2)
    s = [[0 for _ in range(k2+1)] for _ in range(k1+1)]
    for i in range(k1+1):
        s[i][0] = indels * i
    for i in range(k2+1):
        s[0][i] = indels * i

    for i in range(1, k1+1):
        for j in range(1, k2+1):
            delta = penalty_matrix(seq1[i-1], seq2[j-1])

            s[i][j] = min(s[i-1][j-1] + delta, s[i-1][j] + indels,
                          s[i][j-1] + indels)
    return s


x, y = 'TACGTCAGC', 'TATGTCATGC'
for row in global_alignment(x, y, indels=8):
    print(row)
