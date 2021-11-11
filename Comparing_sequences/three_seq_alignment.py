def delta(x, y, z, i, j, k): return 1 if x[i] == y[j] == z[k] else 0


def lcs_7(seq1, seq2, seq3):
    """finding the longest common subsequence, the score and its path"""

    s = [[[0 for z in range(len(seq3)+1)] for y in range(len(seq2)+1)]
         for x in range(len(seq1)+1)]
    backtrack = [[[0 for z in range(len(seq3))] for y in range(
        len(seq2))] for x in range(len(seq1))]

    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            for k in range(1, len(seq3)+1):

                # disejajarkan bisa match or mismatch
                aligned = delta(seq1, seq2, seq3, i-1, j-1, k-1)
                s[i][j][k] = max(s[i-1][j][k], s[i][j-1][k], s[i][j][k-1], s[i-1][j-1]
                                 [k], s[i-1][j][k-1], s[i][j-1][k-1], s[i-1][j-1][k-1] + aligned)

                if s[i][j][k] == s[i-1][j][k]:
                    backtrack[i-1][j-1][k-1] = '↓'
                elif s[i][j][k] == s[i][j-1][k]:
                    backtrack[i-1][j-1][k-1] = '→'
                elif s[i][j][k] == s[i][j][k-1]:
                    backtrack[i-1][j-1][k-1] = '⨂'
                elif s[i][j][k] == s[i-1][j-1][k]:
                    backtrack[i-1][j-1][k-1] = '↘'
                elif s[i][j][k] == s[i-1][j][k-1]:
                    backtrack[i-1][j-1][k-1] = '⇓'
                elif s[i][j][k] == s[i][j-1][k-1]:
                    backtrack[i-1][j-1][k-1] = '⇒'
                elif s[i][j][k] == s[i-1][j-1][k-1] + aligned:
                    backtrack[i-1][j-1][k-1] = 'd'

    return s, backtrack


def output_lcs_7(backtrack, seq1, seq2, seq3):
    """Returning three sequence that already aligned for higher score"""
    i = len(seq1)
    j = len(seq2)
    k = len(seq3)

    output = []
    for _ in range(3):  # karena ada tiga sequence
        output.append([])

    if i == 0 and j == 0 and k == 0:
        return ''
    while i > 0 and j > 0 and k > 0:
        if backtrack[i-1][j-1][k-1] == 'd':
            output[0].append(seq1[i-1])
            output[1].append(seq2[j-1])
            output[2].append(seq3[k-1])
            i -= 1
            j -= 1
            k -= 1
        elif backtrack[i-1][j-1][k-1] == '↓':
            output[0].append(seq1[i-1])
            output[1].append('-')
            output[2].append('-')
            i -= 1
        elif backtrack[i-1][j-1][k-1] == '→':
            output[0].append('-')
            output[1].append(seq2[j-1])
            output[2].append('-')
            j -= 1
        elif backtrack[i-1][j-1][k-1] == '⨂':
            output[0].append('-')
            output[1].append('-')
            output[2].append(seq3[k-1])
            k -= 1
        elif backtrack[i-1][j-1][k-1] == '↘':
            output[0].append(seq1[i-1])
            output[1].append(seq2[j-1])
            output[2].append('-')
            i -= 1
            j -= 1
        elif backtrack[i-1][j-1][k-1] == '⇓':
            output[0].append(seq1[i-1])
            output[1].append('-')
            output[2].append(seq3[k-1])
            i -= 1
            k -= 1
        elif backtrack[i-1][j-1][k-1] == '⇒':
            output[0].append('-')
            output[1].append(seq2[j-1])
            output[3].append(seq3[k-1])
            j -= 1
            k -= 1

    while i > 0:
        output[0].append(seq1[i-1])
        output[1].append('-')
        output[2].append('-')
        i -= 1

    while j > 0:
        output[0].append('-')
        output[1].append(seq2[j-1])
        output[2].append('-')
        j -= 1

    while k > 0:
        output[0].append('-')
        output[1].append('-')
        output[2].append(seq3[k-1])
        k -= 1

    return output[0][::-1], output[1][::-1], output[2][::-1]


def multiple_alignment(seq1, seq2, seq3):

    matrix_score, backtracking = lcs_7(seq1, seq2, seq3)
    align1, align2, align3 = output_lcs_7(backtracking, seq1, seq2, seq3)
    score = matrix_score[-1][-1][-1]

    return str(score), ''.join(align1), ''.join(align2), ''.join(align3)


if __name__ == '__main__':
    with open('E:rosalind//rosalind_ba5m.txt', 'r') as file:
        seq_1 = file.readline().strip()
        seq_2 = file.readline().strip()
        seq_3 = file.readline().strip()
    alignment = multiple_alignment(seq_1, seq_2, seq_3)
    print('\n'.join(alignment))
