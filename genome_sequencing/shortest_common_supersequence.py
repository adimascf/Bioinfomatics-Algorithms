#!/usr/bin/python3
import sys


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


def find_scs(lcs_seq, v, w):

    result = ""

    i, j, k = 0, 0, 0
    n, m, o = len(v), len(w), len(lcs_seq)

    while i < n and j < m and k < o:

        if v[i] == w[j] and v[i] == lcs_seq[k] and w[j] == lcs_seq[k]:
            result += lcs_seq[k]
            i += 1
            j += 1
            k += 1

        elif v[i] != lcs_seq[k]:
            result += v[i]
            i += 1

        elif w[j] != lcs_seq[k]:
            result += w[j]
            j += 1

    while i < n:
        result += v[i]
        i += 1

    while j < m:
        result += w[j]
        j += 1
    return result


def main(problem):

    with open(problem) as file:
        content = file.readlines()
        seq1 = content[0].strip()
        seq2 = content[1].strip()

    _, b = longest_common_subseq(seq1, seq2)
    lcs = ouput_seq(b, seq1, seq2)
    print(find_scs(lcs, seq1, seq2))


if __name__ == '__main__':
    problem = sys.argv[1]
    main(problem)
