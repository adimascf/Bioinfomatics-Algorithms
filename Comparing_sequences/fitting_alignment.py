def delta(x, y, i, j): return 1 if x[i] == y[j] else -1


def lcs_3(v, w):
    """finding the longest common subsequence, the score and its path"""
    indels = -1
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

    last_index = 0  # stroring the last highest index of v, ini dipakai sebagai posisi awal backtracking

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):

            match_mis = delta(v, w, i-1, j-1)
            s[i][j] = max(0, s[i-1][j] + indels, s[i][j-1] +
                          indels, s[i-1][j-1] + match_mis)

            if s[last_index][len(w)] <= s[i][len(w)]:
                last_index = i

            if s[i][j] == s[i-1][j] + indels:
                backtrack[i-1][j-1] = '↓'
            elif s[i][j] == s[i][j-1] + indels:
                backtrack[i-1][j-1] = '→'
            elif s[i][j] == s[i-1][j-1] + match_mis:
                backtrack[i-1][j-1] = '↘'

    return (s, backtrack), last_index


# i index for v, j index for w, i and j is the index of the sink (last)
def output_lcs_3(backtrack, v, w, last_idx):
    """Returning two sequence that already aligned for higher score"""
    i = last_idx
    j = len(w)

    output = []
    for _ in range(2):  # karena ada dua sequence
        output.append([])

    if i == 0 and j == 0:
        return ''

    while i > 0 and j > 0:  # if j == 0, means the first character of sequence w had been added and this ends the while loop
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


def fitting_alignment():
    """Input: Two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100.
    Output: A highest-scoring fitting alignment between v and w.
    Use the simple scoring method in which matches count +1 and both the mismatch and indel penalties are 1."""

    with open('E://rosalind//rosalind_ba5h.txt', 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()

    sb, idx = lcs_3(seq1, seq2)
    print(sb[0][idx][-1])
    s1, s2 = output_lcs_3(sb[1], seq1, seq2, idx)
    print(''.join(s1))
    print(''.join(s2))


if __name__ == '__main__':
    fitting_alignment()
