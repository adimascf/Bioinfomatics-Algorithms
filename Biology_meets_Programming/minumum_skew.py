def SkewArray(Genome):
    skew = [0]
    for i in range(0, len(Genome)):
        if Genome[i] == 'A' or Genome[i] == 'T':
            skew.append(skew[-1])
        elif Genome[i] == 'G':
            skew.append(skew[-1]+1)
        elif Genome[i] == 'C':
            skew.append(skew[-1]-1)
    return skew


def MinimumSkew(Genome):
    skew = SkewArray(Genome)
    minimum = min(skew)
    find = [str(i) for i, val in enumerate(skew) if val == minimum]
    return ' '. join(find)


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba1f.txt') as ff:
        genome = ff.read().strip()

    print(MinimumSkew(genome))

if __name__ == '__main__':
    main()
