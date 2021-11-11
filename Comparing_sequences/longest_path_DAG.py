from collections import defaultdict
import collections


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


def topsort_khan(graph):
    """Sorting the nodes in order from a given adjacency list"""
    result = []
    indegrees = count_in(graph)
    queue = collections.deque()

    for node, val in indegrees.items():
        if val == 0:
            queue.append(node)

    while len(queue) > 0:

        vertex = queue.popleft()
        result.append(vertex)
        for node in graph[vertex]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                queue.append(node)
    return result


def lp_backtrack(source, nodes, in_dict):
    """Returning a length form source to a certain node and its bracktracking"""
    backtrack = dict()
    length = dict()
    is_source_found = False
    for n in nodes:
        if not is_source_found:
            if n == source:
                length[n] = 0
                is_source_found = True
            else:
                continue
        if not n in in_dict:
            continue
        else:
            max_length = -999999
            prev_node = None
            for m, weight in in_dict[n].items():
                if m in length:
                    curr_length = length[m] + weight
                    if curr_length > max_length:
                        max_length = curr_length
                        prev_node = m

            if prev_node != None:
                length[n] = max_length
                backtrack[n] = prev_node
    return length, backtrack


def output_lp(backtrack, source, sink):
    """returning a path from backtracking that already created"""
    path = [sink]
    n = sink
    while n in backtrack:
        if n == source:
            return path
        n = backtrack[n]
        path.insert(0, n)
    return path

def main():

    with open('E://rosalind/rosalind_ba5d.txt', 'r') as file:
        start = file.readline().strip()
        end = file.readline().strip()
        graph = defaultdict(list)
        nodes = set()
        raw_graph = file.readlines()

    for g in raw_graph:
        item = g.strip().split('->')
        nfrom = item[0]
        graph[nfrom]
        nodes.add(nfrom)

    for key, val in graph.items():
        for g in raw_graph:
            item = g.strip().split('->')
            nto = item[1].split(':')[0]
            weight = int(item[1].split(':')[1])
            nodes.add(nto)
            if key == item[0]:
                val.append(nto)


    with open('E://rosalind/rosalind_ba5d.txt', 'r') as f:
        data = f.read().strip().split()
        out_dict = dict()
        in_dict = dict()
        graph_in = defaultdict(list)
        nodes = []
        for e in data[2:]:
            edge = e.split('->')
            nfrom = edge[0]
            nto = edge[1].split(':')[0]
            weight = int(edge[1].split(':')[1])
            if nfrom not in nodes:
                nodes.append(nfrom)
            if nto not in nodes:
                nodes.append(nto)
            if nfrom not in out_dict:
                out_dict[nfrom] = dict()
                out_dict[nfrom][nto] = weight
            else:
                out_dict[nfrom][nto] = weight
            if nto not in in_dict:
                in_dict[nto] = dict()
                graph_in[nto] = []
                in_dict[nto][nfrom] = weight
                graph_in[nto].append(nfrom)
            else:
                in_dict[nto][nfrom] = weight
                graph_in[nto].append(nfrom)

    topological_sort = topsort_khan(graph)
    length, backtrack = lp_backtrack(start, topological_sort, in_dict)
    path = output_lp(backtrack, start, end)
    print(length[end])
    print('->'.join(path))

if __name__ == '__main__':
    main()
