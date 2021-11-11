from out_indegrees import count_in, count_out


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


def main():
    with open('E://problem_dna_sequencing/cs_nm.txt', 'r') as data:
        graph_cs = dict((line.strip().split(' -> ') for line in data))
        for key in graph_cs:
            graph_cs[key] = graph_cs[key].split(',')

    maximal = find_max_nonbranc(graph_cs)
    for arr in maximal:
        print('->'.join(arr))


if __name__ == '__main__':
    main()
