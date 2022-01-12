from io import StringIO
from Bio import Phylo


def distance_between_two(list_pairs):
    """Using Biophython module, get the distance between two leaf in the
    newick tree format."""

    result = []
    for newick_tree, pair in list_pairs:
        leaf1, leaf2 = pair.split(' ')
        tree = Phylo.read(StringIO(newick_tree), 'newick')
        clades = tree.find_clades()
        for clade in clades:
            clade.branch_length = 1  # set the brach length
        dist = tree.distance(leaf1, leaf2)
        result.append(dist)
    return result


with open('E:rosalind/rosalind_nwck.txt', 'r') as f:
    pairs_test = [i.split('\n') for i in f.read().strip().split('\n\n')]
print(*distance_between_two(pairs_test))
