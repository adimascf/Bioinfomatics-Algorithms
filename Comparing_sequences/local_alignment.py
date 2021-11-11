
with open('E://problem_dna_sequencing/pam250.txt', 'r') as f:
        content_list = [line.strip() for line in f.readlines()]
        amino_acids = content_list[0].split()
        pam250 = {}
        for i in range(len(amino_acids)):
            for j in range(len(amino_acids)):
                pam250[amino_acids[i] + amino_acids[j]
                       ] = int(content_list[i+1].split()[j+1])

def lcs_1(v, w):
    """finding the longest common subsequence, the score and its path"""
    sigma = 5
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

    # for storing the index of the highest score in the matrix, inizitalise with index (0, 0) which has score 0
    idx_1, idx_2 = 0, 0

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            match = pam250[v[i-1] + w[j-1]]
            s[i][j] = max(0, s[i-1][j]-sigma, s[i][j-1] -
                          sigma, s[i-1][j-1] + match)

            if s[i][j] > s[idx_1][idx_2]:
                idx_1, idx_2 = i, j

            if s[i][j] == 0:
                backtrack[i-1][j-1] = 'source'
            elif s[i][j] == s[i-1][j] - sigma:
                backtrack[i-1][j-1] = 'south'
            elif s[i][j] == s[i][j-1] - sigma:
                backtrack[i-1][j-1] = 'east'
            elif s[i][j] == s[i-1][j-1] + match:
                backtrack[i-1][j-1] = 'southeast'

    return (s, backtrack), (idx_1, idx_2)


# i index for v, j index for w, i and j is the index of the sink (last)
def output_lcs_1(s, backtrack, v, w, hi_1, hi_2):
    """Returning two sequence that already aligned for higher score"""
    i = hi_1  # start backtracking from the highest score index in matrix s
    j = hi_2

    output = []
    for _ in range(2):  # karena ada dua sequence
        output.append([])

    if i == 0 and j == 0:
        return ''
    while s[i][j] != 0:  # backtracking will stop when ketemu score 0 in the matrix
        if backtrack[i-1][j-1] == 'southeast':
            output[0].append(v[i-1])
            output[1].append(w[j-1])
            i -= 1
            j -= 1
        elif backtrack[i-1][j-1] == 'south':
            output[0].append(v[i-1])
            output[1].append('-')
            i -= 1
        elif backtrack[i-1][j-1] == 'east':
            output[0].append('-')
            output[1].append(w[j-1])
            j -= 1

    return output[0][::-1], output[1][::-1]


def local_alignment():
    """Input: Two protein strings written in the single-letter amino acid alphabet.
    Output: The maximum score of a local alignment of the strings,
    followed by a local alignment of these strings achieving the maximum score.
    Use the PAM250 scoring matrix for matches and mismatches as well as the indel penalty σ = 5."""


    with open('E:rosalind//rosalind_ba5f.txt', 'r') as file:
        s1 = file.readline().strip()
        s2 = file.readline().strip()

    # tuple dalam tuple
    # mb nyimpen matrix score atau s dan bactracking code,
    mb, index = lcs_1(s1, s2)
    # index has index for row and column for the highest core in the matrix

    print(mb[0][index[0]][index[1]])
    seq1, seq2 = output_lcs_1(mb[0], mb[1], s1, s2, index[0], index[1])
    print(''.join(seq1))
    print(''.join(seq2))


if __name__ == '__main__':
    local_alignment()
