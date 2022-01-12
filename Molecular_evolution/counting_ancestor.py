"""
An unrooted binary tree is a tree in which every node has degree equal to 1 or 3.
All internal nodes have 3 degree, all leaves have 1 degree

Jumlah dari degree node adalah dua kali lipat dari jumlah edges (karena setiap edges dihitung dua kali,
1 - 2 dan 2 - 1). Soo,, let k = number of internal nodes and n is num of leaves.
3k + n = 2 . (n+k-1)
k = n - 2
"""


def counting_phylgenetic_ancestor(num_leaves):
    """Get the number of internal nodes from a given an unrooted binary tree with n leaves"""
    return num_leaves - 2


with open('E:rosalind/rosalind_inod.txt', 'r') as f:
    num_leaves_test = int(f.readline().strip())

print(counting_phylgenetic_ancestor(num_leaves_test))
