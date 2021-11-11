
def HammingDistance(p, q):
    """Returning hamming distance/SNIP between two sequencing. Input two string with equal length"""
    if len(p) == len(q):
        hamming_distance = 0
        for i in range(len(p)):
            if p[i] != q[i]:
                hamming_distance += 1
            else:
                pass
    else:
        hamming_distance = 'p and q must in the equal length'

    return hamming_distance


def ApproximatePatternMatching(Text, Pattern, d):
    positions = []  # initializing list of positions
    for i in range(len(Text)-len(Pattern)+1):
        p = Text[i:i+len(Pattern)]
        if HammingDistance(p, Pattern) <= d:
            positions.append(str(i))
    return ' '.join(positions)


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba1h.txt') as file:
        pat = file.readline().strip()
        ome_and_d = file.read().split()
        genome = ome_and_d[0]
        d = int(ome_and_d[1])

        print(ApproximatePatternMatching(genome, pat, d))

if __name__ == '__main__':
    main()
