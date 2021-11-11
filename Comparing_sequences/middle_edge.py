import math
with open('E://problem_dna_sequencing//blosum62.txt', 'r') as f:
    content_list = [line.strip() for line in f.readlines()]
    amino_acids = content_list[0].split()
    blosum62 = {}
    for i in range(len(amino_acids)):
        for j in range(len(amino_acids)):
            blosum62[amino_acids[i] + amino_acids[j]
                     ] = int(content_list[i+1].split()[j+1])


def middle_edge(v, w):
    """Finding a middle edge in the alignment graph in the form (i, j) (k, l), where (i, j) connects to (k, l). 
    To compute scores, use the BLOSUM62 scoring matrix and a (linear) indel penalty equal to 5."""

    m = len(v)
    n = len(w)

    sigma = 5

    s_source = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    s_sink = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    s_sum = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]

    for i in range(len(v)+1):
        s_source[i][0] = - i * sigma
        s_sink[m-i][n] = - i * sigma
    for j in range(len(w)+1):
        s_source[0][j] = - j * sigma
        s_sink[m][n-j] = - j * sigma

    for i in range(1, m+1):
        for j in range(1, n+1):
            match_source = blosum62[v[i-1] + w[j-1]]
            s_source[i][j] = max(s_source[i-1][j]-sigma, s_source[i]
                                 [j-1]-sigma, s_source[i-1][j-1] + match_source)

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            match_sink = blosum62[v[i] + w[j]]
            s_sink[i][j] = max(s_sink[i+1][j]-sigma, s_sink[i]
                               [j+1]-sigma, s_sink[i+1][j+1] + match_sink)

    middle_col = math.floor(n/2)
    row = 0  # Inizialitation with zero
    adj_col = 0
    adj_row = 0

    # Finding the middle node, node in the middle column which has highest score
    for i in range(m+1):
        for j in range(n+1):
            s_sum[i][j] = s_source[i][j] + s_sink[i][j]
            if s_sum[row][middle_col] < s_sum[i][middle_col]:
                row, middle_col = i, middle_col

    # Finding the adjacency for the middle node, which is a node which has same score with the middle node
    if m + 1 > row + 1:
        if s_sum[row][middle_col] == s_sum[row+1][middle_col+1]:
            adj_row, adj_col = row + 1, middle_col + 1

        elif s_sum[row][middle_col] == s_sum[row+1][middle_col]:
            adj_row, adj_col = row + 1, middle_col
    adj_row, adj_col = row, middle_col + 1


    middle_node = row, middle_col
    connect_to = adj_row, adj_col

    return middle_node, connect_to


with open('E:rosalind//rosalind_ba5k.txt', 'r') as file:
    seq_1 = file.readline().strip()
    seq_2 = file.readline().strip()

for node in middle_edge(seq_1, seq_2):
    print(node, end=' ')
