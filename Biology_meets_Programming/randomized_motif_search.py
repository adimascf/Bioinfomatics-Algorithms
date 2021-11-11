import random


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


# Then copy your ProfileMostProbableKmer(Text, k, Profile) and Pr(Text, Profile) functions here.
def ProfileMostProbableKmer(text, k, profile):
    # storing k-mers from a given text
    substext_list = []
    for i in range(len(text)-k+1):
        substext_list.append(text[i:i+k])

    # converting into dict
    substext_dict = {}
    for sub in substext_list:
        substext_dict[sub] = 0

    # calculating pr
    for key, val in substext_dict.items():
        substext_dict[key] = Pr(key, profile)

    # finding the max value
    return max(substext_dict, key=substext_dict.get)


def Pr(Text, Profile):
    result = 1
    for i in range(len(Text)):
        result = result * Profile[Text[i]][i]
    return result

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)


def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


def Motifs(Profile, Dna):
    t = len(Dna)
    k = len(Profile['A'])
    motifs = []
    for i in range(t):
        motifs.append(ProfileMostProbableKmer(Dna[i], k, Profile))
    return motifs


def RandomMotifs(Dna, k, t):
    t = len(Dna)
    l = len(Dna[0])
    random_motifs = []
    for i in range(t):
        random_num = random.randint(0, l-k)
        random_motifs.append(Dna[i][random_num:random_num+k])
    return random_motifs


def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba2f.txt') as f:
        k, t = f.readline().split(' ')
        dna_list = []
        for line in f:
            dna_list.append(line.strip())
        k = int(k)
        t = int(t)

    BestMotifs = RandomizedMotifSearch(dna_list, k, t)
    for _ in range(1000):
        m = RandomizedMotifSearch(dna_list, k, t)
        if Score(m) < Score(BestMotifs):
            BestMotifs = m
    for item in BestMotifs:
        print(item)


if __name__ == '__main__':
    main()
