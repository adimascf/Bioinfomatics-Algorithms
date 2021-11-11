from random import randint


def hamming_distance(seq1, seq2):
    """return number of difference char fro two same length string"""
    result = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            result += 1
    return result


def probability(sequence, profile):

    result = 1
    for i, base in enumerate(sequence):
        result *= profile[base][i]
    return result


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


def find_motifs(profile, arr_sequences):
    """Finding motifs from a given a list of sequences and profile matrix
    input parameters are a profile dictionary and a list of stings, return a list of motifs"""
    t = len(arr_sequences)
    k = len(profile['A'])
    motifs = []
    for i in range(t):
        motifs.append(profile_most_probable_kmer(arr_sequences[i], k, profile))
    return motifs


def randomized_motif_search(arr_seqeunces, k, t):
    """Finding regulatory motifs in a list of sequences (using randomized algorithm)
    inpur parameters are a list of string, integer k, t, N"""

    # Generates randomized motifs first
    motifs = []
    for seq in arr_seqeunces:
        i = randint(0, len(seq)-k)
        motifs.append(seq[i:i+k])

    best_motifs = motifs[:]
    condition = True
    while condition:
        get_profile = profile_with_pseudocounts(motifs)
        motifs = find_motifs(get_profile, arr_seqeunces)

        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            # the time the function return an output, this will terminate a while loop
            return best_motifs


def iteration_random_motif(arr_seqeunces, k, t, number=1000):

    last_motifs = randomized_motif_search(arr_seqeunces, k, t)

    for _ in range(number):
        best_motifs = randomized_motif_search(arr_seqeunces, k, t)

        print(score(last_motifs))

        if score(best_motifs) < score(last_motifs):
            last_motifs = best_motifs

    return last_motifs


