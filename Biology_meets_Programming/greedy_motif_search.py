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


def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in 'ACGT':
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    for symbol in 'ACGT':
        profile[symbol] = []
        for j in range(k):
            profile[symbol].append(0)

    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            profile[symbol][j] += 1

    for key in profile.keys():
        profile[key] = [i/len(Motifs) for i in profile[key]]

    return profile


def Consensus(Motifs):
    k = len(Motifs[0])

    count = Count(Motifs)  # we call count function above

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


def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba2d.txt') as f:
        k, t = f.readline().split(' ')
        dna_list = []
        for line in f:
            dna_list.append(line.strip())

    for item in GreedyMotifSearch(dna_list, int(k), int(t)):
        print(item)

if __name__ == '__main__':
    main()
