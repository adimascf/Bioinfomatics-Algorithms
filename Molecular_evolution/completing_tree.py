"""
Tree of life represented as a connected graph without cycle and has following characteristics:
- Every tree with at least two nodes has at least two leaves.
- Every tree with n nodes has n - 1 edges;
- there exists exactly one path connecting every pair of nodes in a tree.
"""


def completing_tree(edges, num_nodes):
    """Get minimum number of edges that can be added to the graph to produce a tree.
    Input paramters are edges in a list of lists and integer of nodes number
    Returns integer"""
    num_edges = len(edges)
    return num_nodes - 1 - num_edges  # Every tree with n nodes has n - 1 edges


with open('E:rosalind/rosalind_tree.txt', 'r') as f:
    num_nodes_test = int(f.readline())
    edges_test = []
    all_edges = f.readlines()
    for edge in all_edges:
        edge = edge.strip().split(' ')
        edge = list(map(lambda x: int(x), edge))
        edges_test.append(edge)

print(completing_tree(edges_test, num_nodes_test))
