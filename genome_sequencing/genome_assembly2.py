from error_correction_reads import reverse_complement


def genome_assembly(reads):
    """Finds a cyclic superstring of minimal length containing every read or its reverse complement"""

    # k is some positive integer, and we don't know exactly
    k = 1
    while k < len(reads[0]):

        # creates mers from reads with every k value
        mers = set()
        for kmer in reads:
            for i in range(k):
                mers.add(kmer[i:len(kmer) - k + i + 1])
                mers.add(reverse_complement(kmer[i:len(kmer) - k + i + 1]))

        # creates edges of the brujin graph
        length_kmer = len(list(mers)[0])
        edge = lambda mer: (mer[:length_kmer - 1], mer[1:length_kmer])
        edges = [edge(mer) for mer in mers]

        # construct the cyclic superstring from the edges
        result = []
        # find two directed edges
        j = 0
        while j < 2:
            temp_kmer = edges.pop(0)
            cyclic = temp_kmer[0][-1]
            while temp_kmer[1] in [item[0] for item in edges]:
                cyclic += temp_kmer[1][-1]
                for i, pair in enumerate(edges):
                    if pair[0] == temp_kmer[1]:
                        idx = i
                temp_kmer = edges.pop(idx)
            result.append(cyclic)
            j += 1

        if len(edges) == 0:
            break

        k += 1
    return result


with open('E:rosalind/rosalind_gasm.txt', 'r') as f:
    read_test = f.readlines()
    read_test = list(map(lambda x: x.strip(), read_test))
seq1, seq2 = genome_assembly(read_test)
if seq1 < seq2:
    print(seq1)
else:
    print(seq2)