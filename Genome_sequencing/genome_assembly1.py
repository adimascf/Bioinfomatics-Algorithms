def genome_assembly(reads):
    """Assembly genome from reads with perfect coverage.
    The assumption is all reads derive from the same strand (unrealistic)"""

    length_reads = len(reads)

    debrujin_graph = {}
    for read1 in reads:
        for read2 in reads:
            # perfect coverage, reads begin at every position in the genome
            # # r[1:k], r[2:k+1]
            if read2.startswith(read1[1:]):
                debrujin_graph[read1] = read2

    cyclic_superstring = reads[0]

    i = 0
    while len(cyclic_superstring) != length_reads:  # because perfect coverage
        temp = cyclic_superstring[i:]
        cyclic_superstring += debrujin_graph[temp][-1]
        i += 1
    return cyclic_superstring


with open('E:rosalind/rosalind_pcov.txt', 'r') as f:
    reads_test = f.readlines()
    reads_test = list(map(lambda x: x.strip(), reads_test))
print(genome_assembly(reads_test))