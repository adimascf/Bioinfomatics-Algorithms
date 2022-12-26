from collections import defaultdict


def count_in(graph_dict):
    """Counting indegrees for every node in a given graph"""
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


def count_out(graph_dict):
    """Counting outdegrees for every node in a given graph"""
    out_counts = defaultdict(int)
    for key, val in graph_dict.items():
        for v in val:
            if v not in out_counts:
                out_counts[v] = 0
        out_counts[key] = len(val)
    return out_counts
