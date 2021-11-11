

with open('E://problem_dna_sequencing//blosum62.txt', 'r') as f:
    content_list = [line.strip() for line in f.readlines()]
    amino_acids = content_list[0].split()
    blosum62 = {}
    for i in range(len(amino_acids)):
        for j in range(len(amino_acids)):
            blosum62[amino_acids[i] + amino_acids[j]
                     ] = int(content_list[i+1].split()[j+1])


def lcs_5(v, w):
    """finding the longest common subsequence, the score and its path"""
    sigma = 11
    epilson = 1

    s_upper = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    s = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    s_lower = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]

    backtrack = [[0 for j in range(len(w))] for i in range(len(v))]

    for i in range(len(v)+1):
        s[i][0] = 0 if i == 0 else - sigma - (epilson*i-1)
        s_lower[i][0] = 0 if i == 0 else - sigma - (epilson*i-1)
        s_upper[i][0] = 0 if i == 0 else float('-inf')

    for j in range(len(w)+1):
        s[0][j] = 0 if j == 0 else - sigma - (epilson*j-1)
        s_lower[0][j] = 0 if j == 0 else float('-inf')
        s_upper[0][j] = 0 if j == 0 else - sigma - (epilson*j-1)

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            match = blosum62[v[i-1] + w[j-1]]

            s_lower[i][j] = max(s_lower[i-1][j] - epilson, s[i-1][j] - sigma)
            s_upper[i][j] = max(s_upper[i][j-1] - epilson, s[i][j-1] - sigma)

            s[i][j] = max(s_lower[i][j], s[i-1][j-1] + match, s_upper[i][j])

            if s[i][j] == s_lower[i][j]:
                backtrack[i-1][j-1] = '↓'
            elif s[i][j] == s_upper[i][j]:
                backtrack[i-1][j-1] = '→'
            elif s[i][j] == s[i-1][j-1] + match:
                backtrack[i-1][j-1] = '↘'

    return s, backtrack


# i index for v, j index for w, i and j is the index of the sink (last)
def output_lcs_5(backtrack, v, w):
    """Returning two sequence that already aligned for higher score"""
    i = len(v)
    j = len(w)

    output = []
    for _ in range(2):  # karena ada dua sequence
        output.append([])

    if i == 0 and j == 0:
        return ''
    while i > 0 and j > 0:
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
    while i > 0:
        output[0].append(v[i-1])
        output[1].append('-')
        i -= 1
    while j > 0:
        output[0].append('-')
        output[1].append(w[j-1])
        j -= 1

    return output[0][::-1], output[1][::-1]


def global_alignment_affine_gaps():

    with open('E:rosalind//rosalind_ba5j.txt', 'r') as file:
        seq_1 = file.readline().strip()
        seq_2 = file.readline().strip()

    s, b = lcs_5(seq_1, seq_2)
    print(s[-1][-1])
    seq1, seq2 = output_lcs_5(b, seq_1, seq_2)
    print(''.join(seq1))
    print(''.join(seq2))


if __name__ == '__main__':
    global_alignment_affine_gaps()
