with open('E://problem_dna_sequencing//blosum62.txt', 'r') as f:
    content_list = [line.strip() for line in f.readlines()]
    amino_acids = content_list[0].split()
    blosum62 = {}
    for i in range(len(amino_acids)):
        for j in range(len(amino_acids)):
            blosum62[amino_acids[i] + amino_acids[j]
                     ] = int(content_list[i+1].split()[j+1])

with open('E:problem_dna_sequencing//dataset_247_3.txt', 'r') as file:
    seq_1 = file.readline().strip()
    seq_2 = file.readline().strip()


def lcs(v, w):

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
        s[i][0] = - i * sigma
    for j in range(len(w)+1):
        s[0][j] = - j * sigma

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            match = blosum62[v[i-1] + w[j-1]]
            s[i][j] = max(s[i-1][j]-sigma, s[i][j-1] -
                          sigma, s[i-1][j-1] + match)

            if s[i][j] == s[i-1][j] - sigma:
                backtrack[i-1][j-1] = 'south'
            elif s[i][j] == s[i][j-1] - sigma:
                backtrack[i-1][j-1] = 'east'
            elif s[i][j] == s[i-1][j-1] + match:
                backtrack[i-1][j-1] = 'southeast'
    return s, backtrack


# i index for v, j index for w, i and j is the index of the sink (last)
def output_lcs(backtrack, v, w):
    """Returning a longest common subsequence"""
    i = len(v)
    j = len(w)

    output = []
    for _ in range(2):  # karena ada dua sequence
        output.append([])

    if i == 0 and j == 0:
        return ''
    while i > 0 and j > 0:
        if backtrack[i-1][j-1] == 'southeast':
            output[0].append(v[i-1])
            output[1].append(w[j-1])
            i -= 1
            j -= 1
        elif backtrack[i-1][j-1] == 'south':
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


def global_alignment():
    """Input: Two protein strings written in the single-letter amino acid alphabet.
    Output: The maximum alignment score of these strings followed by an alignment achieving this maximum score. 
    Use the BLOSUM62 scoring matrix for matches and mismatches as well as the indel penalty σ = 5."""

    with open('E:rosalind//rosalind_ba5e.txt', 'r') as file:
        seq_1 = file.readline().strip()
        seq_2 = file.readline().strip()

    s, b = lcs(seq_1, seq_2)
    print(s[-1][-1])
    seq1, seq2 = output_lcs(b, seq_1, seq_2)
    print(''.join(seq1))
    print(''.join(seq2))


if __name__ == '__main__':
    global_alignment()
