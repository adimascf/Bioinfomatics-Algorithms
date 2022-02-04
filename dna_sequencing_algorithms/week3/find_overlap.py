from itertools import permutations
from collections import defaultdict


def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match


def find_all_ovelaps(reads, min_length):
    """Naively, find all overlaps for each read in a collection of reads"""
    # result = {}
    count = 0
    for seq1, seq2 in permutations(reads, 2):
        length_overlap = overlap(seq1, seq2, min_length)
        if length_overlap >= min_length:
            # result[(seq1, seq2)] = length_overlap
            count += 1
    return count


def more_efficient_overlaps(reads, k):

    kmers_reads = defaultdict(set)
    for read in reads:
        for i in range(len(read)-k+1):
            mer = read[i:i+k]
            kmers_reads[mer].add(read)

    #  reads_set = set()
    # for read in reads:
    #     suffix = read[-k:]
    #     for r in kmers_reads[suffix]:
    #         reads_set.add(r)
    # return find_all_ovelaps(reads_set, k)

    graph = defaultdict(set)
    for a in reads:
        suffix = a[-k:]
        for b in kmers_reads[suffix]:
            if a != b and overlap(a, b, k):
                graph[a].add(b)
    edges = 0
    for read in graph:
        edges += len(graph[read])
    return edges, len(graph)
