def delta(x, y, i, j): return 1 if x[i] == y[j] else -2


def lcs_4(v, w):
    """finding the longest common subsequence, the score and its path"""
    indels = -2
    s = []
    for i in range(len(v)+1):
        s.append([])
        for j in range(len(w)+1):
            s[i].append(0)

    backtrack = []
    for i in range(len(v)):
        backtrack.append([])
        for j in range(len(w)):
            backtrack[i].append(0)

    for i in range(len(v)+1):
        s[i][0] = 0
    for j in range(len(w)+1):
        s[0][j] = 0

    last_index = 0  # storing for the highest score in last row, index utk posisi awal backtracking dari index w

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):

            match_mis = delta(v, w, i-1, j-1)
            s[i][j] = max(s[i-1][j] + indels, s[i][j-1] +
                          indels, s[i-1][j-1] + match_mis)

            if s[len(v)][last_index] < s[len(v)][j]:
                last_index = j

            if s[i][j] == s[i-1][j] + indels:
                backtrack[i-1][j-1] = '↓'
            elif s[i][j] == s[i][j-1] + indels:
                backtrack[i-1][j-1] = '→'
            elif s[i][j] == s[i-1][j-1] + match_mis:
                backtrack[i-1][j-1] = '↘'

    return (s, backtrack), last_index


# i index for v, j index for w, i and j is the index of the sink (last)
def output_lcs_4(backtrack, v, w, last_idx):
    """Returning two sequence that already aligned for higher score"""
    i = len(v)
    j = last_idx

    output = []
    for _ in range(2):  # karena ada dua sequence
        output.append([])

    if i == 0 and j == 0:
        return ''

    while i > 0 and j > 0:  # it will start backtraking di akhir index v yaitu i dan last idx, which refer to the highest first score in the last row
        if backtrack[i-1][j-1] == '↘':
            output[0].append(v[i-1])
            output[1].append(w[j-1])
            i -= 1
            j -= 1
        elif backtrack[i-1][j-1] == '↓':
            output[0].append(v[i-1])
            output[1].append('-')
            i -= 1
        else:
            output[0].append('-')
            output[1].append(w[j-1])
            j -= 1

    return output[0][::-1], output[1][::-1]


def overlap_alignment():
    """Input: Two strings v and w, each of length at most 1000.
    Output: The score of an optimal overlap alignment of v and w,
    followed by an alignment of a suffix v' of v and a prefix w' of w achieving this maximum score.
    Use an alignment score in which matches count +1 and both the mismatch and indel penalties are 2."""

    with open('E:rosalind//rosalind_ba5i.txt', 'r') as file:
        seq_1 = file.readline().strip()
        seq_2 = file.readline().strip()

    sb, idx = lcs_4(seq_1, seq_2)
    print(sb[0][-1][idx])
    seq1, seq2 = output_lcs_4(sb[1], seq_1, seq_2, idx)
    print(''.join(seq1))
    print(''.join(seq2))


if __name__ == '__main__':
    overlap_alignment()
