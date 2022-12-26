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


def eulerian_path(graph_dict):
    """Find eulerian path from adjacency list in dictionary if there is exist"""
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


def string_from_gapped_patterns(rp_list, k, d):
    """Assemble genome from pair end kmers that already in the path of eulerian"""
    read_1 = ''
    read_2 = ''
    for item in rp_list[:-1]:
        read_1 += item[0][0]
        read_2 += item[1][0]
    read_1 += rp_list[-1][0]
    read_2 += rp_list[-1][1]

    str_length = (2*int(k)) + int(d) + len(rp_list) - 1
    read_length = len(read_1)
    match_length = str_length - read_length

    if read_1.endswith(read_2[:-match_length]):
        return read_1 + read_2[-match_length:]
    return read_1, read_2


def read_pairs_problem(pair_end_arr, k, d):
    """Assemble genome from pair ends kmers. Input a list of pair end kmers, length of pair end kmer and distance"""
    k = int(k)
    d = int(d) - 1

    # Generates de brujing graph
    db_dict = defaultdict(list)
    pair_end_arr = sorted(pair_end_arr)
    for mer in pair_end_arr:
        db_dict[mer[0][:-1] + '|' + mer[1][:-1]]
    idx = 0
    for key in db_dict.keys():
        db_dict[key].append(pair_end_arr[idx][0][1:] +
                            '|' + pair_end_arr[idx][1][1:])
        idx += 1
    ep = eulerian_path(db_dict)
    modify_ep = []
    for item in ep:
        modify_ep.append(item.split('|'))
    return string_from_gapped_patterns(modify_ep, k, d)


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba3j.txt', 'r') as file:
        l_kmer, distance = file.readline().split(' ')
        pairs = file.readlines()
        pairs_end = []
        for item in pairs:
            pairs_end.append(item.replace('\n', '').split('|'))
    print(read_pairs_problem(pairs_end, l_kmer, distance))

if __name__ == '__main__':
    main()
