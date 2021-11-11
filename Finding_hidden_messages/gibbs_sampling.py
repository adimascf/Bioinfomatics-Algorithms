from random import uniform, randint


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


def normalize(Probabilities):
    """normalizing probabilites, these probabilities sum to 1
    input parameter is a dictionary of probabilities returns normalized probabilities"""
    sum_all = sum(Probabilities.values())
    result = {}
    for i in Probabilities:
        result[i] = Probabilities[i]/sum_all
    return result


def weighted_die(probabilities):

    count = 0
    random_float = uniform(0, 1)
    for key, val in probabilities.items():
        if val+count < random_float:
            count += val
        else:
            return key


def profile_generate_string(sequence, profile, k):
    """Generating k length mer from a sequence based on a given profile
    input parameters are a sequence of string, dictionary profile
    returns a kmer string"""
    n = len(sequence)
    probabilities = {}

    for i in range(n-k+1):
        probabilities[sequence[i:i+k]] = probability(sequence[i:i+k], profile)

    normalized = normalize(probabilities)
    return weighted_die(normalized)


def gibbs_sampler(arr_sequences, k, t, N):
    """Finding regulatory motifs in a list of sequences (using gibbs sampling)
    inpur parameters are a list of string, integer k, t, N, return motifs which has the minimum score"""

    # Generates randomized motifs first
    motifs = []
    for seq in arr_sequences:
        i = randint(0, len(seq)-k)
        motifs.append(seq[i:i+k])

    best_motifs = motifs.copy()  # copy
    for _ in range(N):
        i = randint(0, t-1)
        exclude_string = arr_sequences[i]
        profile_of_rest = profile_with_pseudocounts(
            best_motifs[:i] + best_motifs[i+1:])
        new_motifs = profile_generate_string(
            exclude_string, profile_of_rest, k)
        renewed_motifs = best_motifs[:i] + [new_motifs] + best_motifs[i+1:]

        if score(best_motifs) > score(renewed_motifs):
            best_motifs = renewed_motifs

    return best_motifs


def iteration_gibbs_sampler(arr_sequences, k, t, N, number_outerloop=20):
    """Re running gibbs sampler to give a good score"""
    last_motifs = []
    for seq in arr_sequences:
        i = randint(0, len(seq)-k)
        last_motifs.append(seq[i:i+k])

    for _ in range(number_outerloop):
        best_motifs = gibbs_sampler(arr_sequences, k, t, N)

        print(f'Immediate score: {score(last_motifs)}')

        if score(best_motifs) < score(last_motifs):
            last_motifs = best_motifs

    return last_motifs


with open('E:finding_ori/dataset_163_4.txt', 'r') as f:
    raw = f.readline().strip().split(' ')
    k_test1, t_test1, N_test1 = list(map(lambda x: int(x), raw))
    sequences_test1 = f.readline().strip().split(' ')

for i in range(10):
    result = iteration_gibbs_sampler(sequences_test1, k_test1, t_test1, N_test1)
    print(f'\nScore in {i}: {score(result)}')
    print('\n')
