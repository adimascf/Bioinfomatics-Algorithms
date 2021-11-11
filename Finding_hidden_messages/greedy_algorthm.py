
def hamming_distance(seq1, seq2):
    """return number of difference char fro two same length string"""
    result = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            result += 1
    return result


def count(motifs):
    """Creating count matrix with pesaudocounts from a given motifs
    input parameter is a list of motifs, returns a dictionary of matrix"""

    k = len(motifs[0])
    result = {symbol: [1] *
              k for symbol in 'ACGT' for _ in range(len(motifs[0]))}

    t = len(motifs)
    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            result[symbol][j] += 1

    return result


def consensus(motifs):
    """creating consesus sequence from a given count matrix
    input paramter is dictionary which has count matrix, return string"""
    count_matrix = count(motifs)

    result = ''
    length_seq = len(count_matrix['A'])

    i = 0
    while i < length_seq:
        temp_char = 'A'
        temp_val = 0
        for key in count_matrix:
            if count_matrix[key][i] > temp_val:
                temp_val = count_matrix[key][i]
                temp_char = key

        result += temp_char
        i += 1

    return result


def score(motifs):
    """Calculating score motifs
    input parameter a list of string motifs and consensus sequence, return integer"""
    result = 0
    find_consensus = consensus(motifs)
    for seq in motifs:
        result += hamming_distance(seq, find_consensus)
    return result


def probability(sequence, profile):

    result = 1
    for i, base in enumerate(sequence):
        result *= profile[base][i]
    return result


def profile_most_probable_kmer(sequence, k, profile):
    """Finding the most probable k length mer in a the sequence
    input paramters are sequence(string) k length (int), and dictionary profile"""
    prob = 0
    most_probable_mer = sequence[0:k]
    # Generates all possible pattern AA..AA to TT..TT
    all_patterns = [sequence[i:i+k] for i in range(len(sequence)-k+1)]

    for mer in all_patterns:
        if probability(mer, profile) > prob:
            prob = probability(mer, profile)
            most_probable_mer = mer
    return most_probable_mer


def profile_with_pseudocounts(motifs):
    """Creating profile matrix with pseudocounts from a given motifs
    input parameter is a list of motifs, returns a dictionary of matrix"""

    k = len(motifs[0])
    # adding 1 (pseudocounts) in each cells in the matrix
    result = {symbol: [1] *
              k for symbol in 'ACGT' for _ in range(len(motifs[0]))}

    t = len(motifs)
    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            result[symbol][j] += 1

    for key in result.keys():
        # because adding pseaudocounts, the deminator is multipled by 2
        result[key] = [i/(len(motifs)*2) for i in result[key]]

    return result


def greedy_motifs_search_pseudocounts(arr_sequence, k, t):
    """Using greedy search algorithm and implementing laplace succession rule,
    finds a collection of k length mer that has minimum score which is best score
    input paramters are a list of sequences, integer k, and integer t. returns a list of k-mer"""

    best_motifs = [seq[0:k] for seq in arr_sequence]

    for i in range(len(arr_sequence[0])-k+1):
        motifs = [arr_sequence[0][i:i+k]]
        for mer in arr_sequence[1:]:
            create_profile = profile_with_pseudocounts(motifs)
            motif_temp = profile_most_probable_kmer(mer, k, create_profile)
            motifs.append(motif_temp)

        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    print(score(best_motifs))
    return best_motifs

with open('E:finding_ori/dataset_163_4.txt', 'r') as f:
    k_test4, t_test4, N = f.readline().strip().split(' ')
    motif_test4 = f.readline().strip().split(' ')

print(*greedy_motifs_search_pseudocounts(motif_test4, int(k_test4), int(t_test4)))