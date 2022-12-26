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


def check_eulerian_cir(graph_dict):
    """Check whether the adjacency list in dictionary has eulrian circle/circuit or not"""
    s = substraction(graph_dict)
    for node, value in s.items():
        if s[node] != 0:
            return 'This is not an eulerian circuit/cycle'
    return 'This is an eulerian circuit/circle'


def check_eulerian_path(graph_dict):
    """Check whether the adjacency list in dictionary has eulrian path or not"""

    s = substraction(graph_dict)
    start_end_nodes = []
    unbalenced_codes = []
    for node, value in s.items():
        if s[node] == -1 or s[node] == 1:
            start_end_nodes.append(node)
        if s[node] != 0:
            unbalenced_codes.append(node)
    if len(unbalenced_codes) and len(start_end_nodes) <= 2:
        return 'This graph eulerian path'
    else:
        return 'There is no an eulerian path'


def input_solution(arr):
    result = arr[0]
    for item in arr[1:]:
        result += '->' + item
    return result


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba3g.txt', 'r') as file:
        adjecency_list = dict((line.strip().split(' -> ') for line in file))
        for key in adjecency_list:
            adjecency_list[key] = adjecency_list[key].split(',')

    print(check_eulerian_cir(adjecency_list))
    print(check_eulerian_path(adjecency_list))
    result = eulerian_path(adjecency_list)
    print(input_solution(result))


if __name__ == '__main__':
    main()
