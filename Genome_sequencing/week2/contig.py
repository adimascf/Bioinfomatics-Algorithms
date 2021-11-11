from collections import defaultdict
from random import choice


def de_brujin_kmers(arr):
    """Creating the brudjin graph from a set of kmers"""
    db_dict = defaultdict(list)
    arr = sorted(arr)
    for mer in arr:
        db_dict[mer[:-1]]  # ini buat prefixnya
    for key in db_dict.keys():
        for i in range(len(arr)):
            if arr[i].startswith(key):
                # ini buat suffix yang bisa nempel di prefix yang sudah dibuat
                db_dict[key].append(arr[i][1:])
    return db_dict


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


def path_to_genom_contigs(arr_contigs):
    """Generate contig from a list that contain of maximal non branching"""
    result = []
    for arr in arr_contigs:
        res = ''
        res = arr[0]
        i = 1
        while i < len(arr):
            res += arr[i][-1]
            i += 1
        result.append(res)
    return ' '.join(result)


def generate_contig(arr_kmers):
    """Generate contig from a given kmers in a list"""
    db = de_brujin_kmers(arr_kmers)
    max_non_branc = find_max_nonbranc(db)
    result = path_to_genom_contigs(max_non_branc)
    return result


def main():
    with open('E://rosalind//rosalind_ba3k.txt') as f:
        contigs_kmers = [line.strip() for line in f.readlines()]

    print(generate_contig(contigs_kmers))


if __name__ == '__main__':
    main()
