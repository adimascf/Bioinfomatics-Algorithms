#!~/miniconda3/bin/python

from utilities import read_fasta
from bio_structures import complement_rna

def catalan_numbers(n):
    """Finding n catalan number using dynamic programming.
    input is interger"""

    track = [0] * (n+1)
    
    track[0], track[1] = 1, 1

    for i in range(2, n+1):
        for j in range(i):
            track[i] += track[j] * track[i-1-j]
    
    return track[-1]

global track_dict
track_dict = {}
def secondary_rna_structures(seq, first, last):
    """Find how many secondary rna structures for a given sequence.
    Using global variable track_dict for tracking number of base mathcing possible with don't cross
    for a certain section of the sequence."""
    # print(first, last)
    seq_len = last - first + 1
    if seq_len % 2 != 0:
        return 0

    if first >= last or first >= len(seq) or first < 0:
        return 1

    # returns the track for solution if one exists
    if (first, last) in track_dict:
        return track_dict[(first, last)]
        
    else:
        curr_base = seq[first]
        count = 0
        pair_base = complement_rna[curr_base]
        for i in range(first+1, last+1, 2):
            if seq[i] == pair_base:
                left = secondary_rna_structures(seq, first+1, i-1)
                right = secondary_rna_structures(seq, i+1, last)
                count += ((left * right))
        track_dict[(first, last)] = count
        return count % 1000000




seq = list(read_fasta("problems/rosalind_cat.txt").values())[0]
# seq = "AUAUAUAUAUAUAUAUAU"
print(secondary_rna_structures(seq, 0, len(seq)-1))
print(max(list(track_dict.values())) % 1000000)



