from collections import defaultdict
from itertools import permutations

from sympy import prefixes


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


def scs(ss, min_length):
    """Find shortest common superstring of given strings, checking all
    possible permutations between string"""
    shortest_sup = None
    perms_list = list(permutations(ss))
    for ssperm in perms_list:
        sup = ssperm[0]
        for i in range(len(ss)-1):
            olen = overlap(ssperm[i], ssperm[i+1], min_length)
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(shortest_sup) > len(sup):
            shortest_sup = sup
    return shortest_sup


def pick_longest_overlap(reads, min_length):
    """Find a pair of reads from a given list of reads with a longest
    suffix/prefix overlap."""
    read_a, read_b = None, None
    best_olen = 0
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, min_length)
        if olen > best_olen:
            best_olen = olen
            read_a, read_b = a, b
    return read_a, read_b, best_olen


def greedy_scs(reads, min_length):
    """Find a shortest common superstring using 'greedy' algorithm, pick
    the longest overlap on every merge untul no edges remain"""
    read_a, read_b, olen = pick_longest_overlap(reads, min_length)
    while olen > 0:
        reads.append(read_a + read_b[olen:])
        reads.remove(read_a)
        reads.remove(read_b)
        read_a, read_b, olen = pick_longest_overlap(reads, min_length)
    return ''.join(reads)


def all_possible_scs(reads, min_length):
    """Find all possible common supersting from a given list of reads."""
    result = set()
    for rs in permutations(reads):
        temp = scs(rs, min_length)
        result.add(temp)
    return sorted(list(result))


def faster_find_longest_overlap(reads, min_length):
    """Create kmer with the corresponded set of reads in dictionary.
    Then, build read key with its overlap reads in  dictionary.
    Finally implement the find the longest overlap algorithm between
    read (key) and its overlap reads (value)."""

    kmers_reads = defaultdict(set)
    for read in reads:
        for i in range(len(read)-min_length+1):
            mer = read[i:i+min_length]
            kmers_reads[mer].add(read)

    graph = defaultdict(set)
    for a in reads:
        sufix = a[-min_length:]
        for b in kmers_reads[sufix]:
            if a != b and overlap(a, b, 3):
                graph[a].add(b)

    read_a, read_b = None, None
    best_olen = 0
    for sufix, prefixes in graph.items():
        prefixes = list(prefixes)
        for prefix in prefixes:
            olen = overlap(sufix, prefix, 3)
            if olen > best_olen:
                best_olen = olen
                read_a, read_b = sufix, prefix
    return read_a, read_b, best_olen


def faster_greedy_scs(reads, min_length):
    """Find a shortest common superstring using 'greedy' algorithm, pick
    the longest overlap on every merge untul no edges remain"""
    total_reads = len(reads)
    i = 0
    read_a, read_b, olen = faster_find_longest_overlap(reads, min_length)
    while olen > 0:
        reads.append(read_a + read_b[olen:])
        reads.remove(read_a)
        reads.remove(read_b)
        i += 1
        print(f'{i/total_reads*100}%')
        read_a, read_b, olen = faster_find_longest_overlap(reads, min_length)
    return ''.join(reads)
