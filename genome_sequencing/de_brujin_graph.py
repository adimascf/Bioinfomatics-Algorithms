from error_correction_reads import reverse_complement


def debrujin_graph(dna_strings):
    """Construct de brujin graph, which is a directed graph for
    representing overlapping string in a collection of k-mers or reads"""

    # Eliminate duplicates, create set that contains k+1 mers
    union_reads = dna_strings + list(
        map(lambda x: reverse_complement(x), dna_strings))
    union_reads = set(union_reads)

    # So, k is ..
    k = len(dna_strings[0]) - 1

    result = []

    for read in union_reads:
        # r[1:k], r[2:k+1]
        temp = (read[:k], read[1:k + 1])
        result.append(temp)

    return sorted(result)


# with open('E:rosalind/rosalind_dbru.txt', 'r') as f:
#     reads_test = f.readlines()
#     reads_test = list(map(lambda x: x.strip(), reads_test))

# for edge in debrujin_graph(reads_test):
#     print('(' + edge[0] + ', ' + edge[1] + ')')