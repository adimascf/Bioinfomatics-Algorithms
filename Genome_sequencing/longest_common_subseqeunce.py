#!/usr/bin/python3

from shortest_superstring import read_fasta


def longest_common_subseq(v, w):

    n, m = len(v), len(w)

    dp_array = [[0]*(m+1) for _ in range(n+1)]

    backtrack = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if v[i-1] == w[j-1]:
                dp_array[i][j] = 1 + dp_array[i-1][j-1]
            else:
                dp_array[i][j] = max(dp_array[i-1][j], dp_array[i][j-1])

            if dp_array[i][j] == dp_array[i-1][j]:
                backtrack[i-1][j-1] = 'south'
            elif dp_array[i][j] == dp_array[i][j-1]:
                backtrack[i-1][j-1] = 'east'
            elif dp_array[i][j] == 1 + dp_array[i-1][j-1]:
                backtrack[i-1][j-1] = 'southeast'

    return dp_array, backtrack


def ouput_seq(backtrack, v, w):

    n, m = len(v), len(w)

    result = ""
    if n == 0 and m == 0:
        return ''
    while n > 0 and m > 0:
        if backtrack[n-1][m-1] == 'southeast':
            result += v[n-1]
            n -= 1
            m -= 1

        elif backtrack[n-1][m-1] == 'south':
            n -= 1

        elif backtrack[n-1][m-1] == 'east':
            m -= 1

    return result[::-1]


seq1, seq2 = read_fasta("../problem-set/rosalind_lcsq.txt").values()

_, b = longest_common_subseq(seq1, seq2)
print(ouput_seq(b, seq1, seq2))
