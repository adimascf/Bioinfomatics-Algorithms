import random


def RandomMotifs(Dna, k, t):
    import random
    t = len(Dna)
    l = len(Dna[0])
    random_motifs = []
    for i in range(t):
        random_num = random.randint(0, l-k)
        random_motifs.append(Dna[i][random_num:random_num+k])
    return random_motifs


def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in 'ACGT':
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    for symbol in 'ACGT':
        profile[symbol] = []
        for j in range(k):
            profile[symbol].append(1)

    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            profile[symbol][j] += 1

    for key in profile.keys():
        # t is added 4 karena append awalnya itu 1 dan ATGC kan 4!!
        profile[key] = [i/(t+4) for i in profile[key]]

    return profile


def WeightedDie(Probabilities):
    count = 0
    random_float = random.uniform(0, 1)
    for key, val in Probabilities.items():
        if val+count < random_float:
            count += val
        else:
            return key


def ProfileGeneratedString(Text, profile):
    n = len(Text)
    probabilities = {}
    k = len(profile['A'])

    for i in range(0, n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)

    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)


def Pr(Text, Profile):
    result = 1
    for i in range(len(Text)):
        result = result * Profile[Text[i]][i]
    return result


def Normalize(Probabilities):
    sum_all = sum(Probabilities.values())
    result = {}
    for i in Probabilities.keys():
        result[i] = Probabilities[i]/sum_all
    return result


def Consensus(Motifs):
    k = len(Motifs[0])

    count = CountWithPseudocounts(Motifs)  # we call count function above

    result = ''
    for j in range(k):
        m = 0
        freq_symbol = ''
        for symbol in 'ACGT':
            if count[symbol][j] > m:
                m = count[symbol][j]
                freq_symbol = symbol
        result += freq_symbol
    return result


def Score(Motifs):
    consensus = Consensus(Motifs)
    k = len(Motifs[0])
    t = len(Motifs)

    final_result = 0

    for i in range(t):
        for j in range(k):
            if Motifs[i][j] != consensus[j]:
                final_result += 1
    return final_result


def GibbsSampler(Dna, k, t, N):
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = Motifs.copy()
    for _ in range(N):
        index_todelete = random.randint(0, t-1)
        deleted_string = Dna[index_todelete]

        profile_of_rest = ProfileWithPseudocounts(
            BestMotifs[:index_todelete] + BestMotifs[index_todelete+1:])

        new_motif = ProfileGeneratedString(deleted_string, profile_of_rest)

        renewed_motifs = BestMotifs[:index_todelete] + \
            [new_motif] + BestMotifs[index_todelete+1:]

        if Score(BestMotifs) > Score(renewed_motifs):

            BestMotifs = renewed_motifs

    return BestMotifs


def main():
    with open('/rosalind_ba2g.txt') as f:
        k, t, N = f.readline().split(' ')
        dna_list = []
        for line in f:
            dna_list.append(line.strip())

        k, t, N = int(k), int(t), int(N)

        BestMotifs = RandomMotifs(dna_list, k, t)
        for i in range(20):  # DIULANG 20 KALI!!
            m = GibbsSampler(dna_list, k, t, N)
            if Score(m) < Score(BestMotifs):
                BestMotifs = m

        for item in BestMotifs:
            print(item)


if __name__ == '__main__':
    main()
