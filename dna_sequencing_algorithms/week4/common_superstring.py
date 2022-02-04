
from itertools import permutations


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
    print(perms_list)
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
