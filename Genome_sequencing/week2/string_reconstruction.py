from collections import defaultdict
from random import choice


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


def substraction(graph_dict):
    """Searching unbalanced degree, if there exist, the substraction will not be 0. Input adjacency list in dictionary"""
    in_count = count_in(graph_dict)
    out_count = count_out(graph_dict)
    substract = defaultdict(int)
    for key, val in in_count.items():
        substract[key] = in_count[key] - out_count[key]
    return substract


def eulerian_path_string_recons(graph_dict):
    """Searching eulerian path if there is exist. Input a adjacency list in dictionary"""
    start = ''
    end = ''
    s = substraction(graph_dict)
    for node, value in s.items():
        if s[node] == -1:
            start = node
        elif s[node] == 1:
            end = node
    graph_dict[end] = [start]
    stack = [end]
    path = []
    while stack != []:
        for key, val in graph_dict.items():
            if len(stack) != 0:
                if key == stack[-1]:
                    pick = [item for item in val]
                    if len(pick) != 0:
                        p = choice(pick)
                        stack.append(p)
                        val.pop(val.index(p))
                    elif len(pick) == 0:
                        path.append(stack[-1])
                        del stack[-1]
    return path[::-1][1:]


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


def path_to_genome(arr):
    result = arr[0]
    for item in arr[1:]:
        result += item[-1]
    return result


def string_reconstruction(arr_kmers):
    """Reconstructing dna sequence from a given set of k mers, and return string"""
    db = de_brujin_kmers(arr_kmers)
    path = eulerian_path_string_recons(db)
    string = path_to_genome(path)
    return string


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba3h.txt') as f:
        k = f.readline()
        contents = [line.strip() for line in f.readlines()]

    print(string_reconstruction(contents))

if __name__ == '__main__':
    main()
