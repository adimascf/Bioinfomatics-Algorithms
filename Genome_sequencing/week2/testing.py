from collections import defaultdict


def count_out(graph_dict):
    """Counts the number of out degree of every node. Input adjacency list in dictionary """
    out_counts = defaultdict(int)
    for key, val in graph_dict.items():
        for v in val:
            if v not in out_counts:
                out_counts[v] = 0
        out_counts[key] = len(val)
    return out_counts


def count_in(graph_dict):
    """Counts the number of in degree of every node. Input adjacency list in dictionary """
    in_counts = defaultdict(int)
    for key, val in graph_dict.items():
        for v in val:
            in_counts[v] += 1
    right = []
    for val in graph_dict.values():
        for v in val:
            right.append(v)
    for key in graph_dict.keys():
        if key not in right:
            in_counts[key] = 0
    return in_counts


def find_max_nonbranc(graph):
    """Finding all maximal non branching from given graph. Input adjancency list in a dictionary, output collection 
    of maximal non branching path """
    paths = []
    nodes_1in_1out = set()
    n_explored = set()
    go_in = count_in(graph)
    go_out = count_out(graph)
    for v in graph.keys():
        if not (1 == go_in[v] and 1 == go_out[v]):
            if go_out[v] > 0:
                for w in graph[v]:
                    nb_path = [v, w]
                    while 1 == go_in[w] and 1 == go_out[w]:
                        n_explored.add(w)
                        u = graph[w][0]
                        nb_path.append(u)
                        w = u
                    paths.append(nb_path)
        else:
            nodes_1in_1out.add(v)
    print(paths)
    for v in nodes_1in_1out:
        if v not in n_explored:
            w = v
            nb_path = []
            while w in nodes_1in_1out:
                nb_path.append(w)
                if w == v and len(nb_path) > 1:
                    paths.append(nb_path)
                    for node in nb_path:
                        n_explored.add(node)
                    break
                w = graph[w][0]
    return paths


with open('E://problem_dna_sequencing/cs_nm.txt', 'r') as data:
    graph_cs = dict((line.strip().split(' -> ') for line in data))
    for key in graph_cs:
        graph_cs[key] = graph_cs[key].split(',')

print(find_max_nonbranc(graph_cs))
