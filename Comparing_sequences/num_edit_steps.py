

def delta(x, y, i, j): return 0 if x[i] == y[j] else -1


def lcs_2(v, w):
    """finding the longest common subsequence, the score and its path"""
    indel_gap = -1
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
        s[i][0] = - i
    for j in range(len(w)+1):
        s[0][j] = - j

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            match_or_mis = delta(v, w, i-1, j-1)

            s[i][j] = max(s[i-1][j] + indel_gap, s[i][j-1] +
                          indel_gap, s[i-1][j-1] + match_or_mis)

            if s[i][j] == s[i-1][j] + indel_gap:
                backtrack[i-1][j-1] = 'south'
            elif s[i][j] == s[i][j-1] + indel_gap:
                backtrack[i-1][j-1] = 'east'
            elif s[i][j] == s[i-1][j-1] + match_or_mis:
                backtrack[i-1][j-1] = 'southeast'

    return s, backtrack


# i index for v, j index for w, i and j is the index of the sink (last)
def output_lcs_2(backtrack, v, w):
    """Returning two sequence that already aligned for higher score"""
    i = len(v)
    j = len(w)

    output = []
    for _ in range(2):  # karena ada dua sequence
        output.append([])

    num_step = 0

    if i == 0 and j == 0:
        return ''
    while i > 0 or j > 0:
        if backtrack[i-1][j-1] == 'southeast':
            output[0].append(v[i-1])
            output[1].append(w[j-1])
            if v[i-1] != w[j-1]:
                num_step += 1
            i -= 1
            j -= 1

        elif backtrack[i-1][j-1] == 'south':
            output[0].append(v[i-1])
            output[1].append('-')
            num_step += 1
            i -= 1

        elif backtrack[i-1][j-1] == 'east':
            output[0].append('-')
            output[1].append(w[j-1])
            num_step += 1
            j -= 1

    return (output[0][::-1], output[1][::-1]), num_step


def edit_distance():

    """Input: Two strings.
    Output: The edit distance between these strings in global alignment.
    """

    with open('E://rosalind//rosalind_ba5g.txt', 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()

    s, b = lcs_2(seq1, seq2)
    print(f'Alignment score: {s[-1][-1]}')
    seq, steps = output_lcs_2(b, seq1, seq2)
    print(''.join(seq[0]))
    print(''.join(seq[1]))
    print(f'Number of steps to align these sequences is: {steps}')


if __name__ == '__main__':
    edit_distance()
