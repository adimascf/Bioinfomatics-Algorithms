from distance_matrix import hamming_distance
from collections import defaultdict


BASES = ['A', 'T', 'C', 'G']


def represent_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def small_parsimony(adj_list):

    # Initialize tree

    Tag = {}
    score_dict = defaultdict(dict)

    nodes = [item for sublist in adj_list for item in sublist]
    nodes = list(set(nodes))

    for v in nodes:
        Tag[v] = 0
        if not represent_integer(v):
            Tag[v] = 1
            len_dna = len(v)
            for pos in range(len_dna):
                score_dict[v][pos] = {}
                char = v[pos]
                for base in BASES:
                    if char == base:
                        score_dict[v][pos][base] = 0
                    else:
                        score_dict[v][pos][base] = float('inf')

    # Calculate scores
    while any(x == 0 for x in list(Tag.values())):
        zero_nodes = [node for node, tag in Tag.items() if tag == 0]
        for zn in zero_nodes:
            childern = [child for parent, child in adj_list if parent == zn]
            if all([Tag[child] == 1 for child in childern]):
                v = zn
                break

        Tag[v] = 1
        for pos in range(len_dna):
            score_dict[v][pos] = {}
            for base in BASES:
                temp = []
                for i, score in score_dict[childern[0]][pos].items():
                    if i == base:
                        temp.append(score)
                    else:
                        temp.append(score+1)
                score_daughter = min(temp)

                temp = []
                for i, score in score_dict[childern[1]][pos].items():
                    if i == base:
                        temp.append(score)
                    else:
                        temp.append(score+1)
                score_son = min(temp)

                score_dict[v][pos][base] = score_daughter + score_son

    return score_dict


def final_tree(adj_list, score_dict):

    nodes = [item for sublist in adj_list for item in sublist]
    nodes = list(set(nodes))
    child_nodes = [child for parent, child in adj_list]

    # finds root
    root = nodes[0]
    idx = 1
    while root in child_nodes:
        root = nodes[idx]
        idx += 1

    # root's label and min parsimony score
    label_dict = defaultdict(str)
    min_parsimony_score = 0
    for pos, scores in score_dict[root].items():
        label_dict[root] += min(scores, key=scores.get)
        min_parsimony_score += min(scores.values())

    # Backtrace
    Tag = {}
    for node in nodes:
        if not represent_integer(node):
            Tag[node] = 1
        else:
            Tag[node] = 0
    Tag[root] = 1

    while any(x == 0 for x in list(Tag.values())):

        one_nodes = [node for node, tag in Tag.items() if tag == 1]
        for node in one_nodes:
            childern = [child for parent, child in adj_list if parent == node]
            if represent_integer(node) and all([Tag[child] == 0 for child in childern]):
                v = node
                break

        daughter_label = ''
        daughter_scores = score_dict[childern[0]]
        for pos, daughter_score in daughter_scores.items():
            parent_later = label_dict[v][pos]
            min_nucs = [nuc for nuc, val in daughter_score.items()
                        if val == min(daughter_score.values())]
            if parent_later in min_nucs:
                daughter_label += parent_later
            else:
                daughter_label += min_nucs[0]

        label_dict[childern[0]] = daughter_label
        Tag[childern[0]] = 1

        son_label = ''
        son_scores = score_dict[childern[1]]
        for pos, son_score in son_scores.items():
            parent_later = label_dict[v][pos]
            min_nucs = [nuc for nuc, val in son_score.items(
            ) if val == min(son_score.values())]
            if parent_later in min_nucs:
                son_label += parent_later
            else:
                son_label += min_nucs[0]

        label_dict[childern[1]] = son_label
        Tag[childern[1]] = 1

    # Create final adjacency list
    fina_adj_list = []
    for edge in adj_list:
        if represent_integer(edge[0]):
            node0 = label_dict[edge[0]]
        else:
            node0 = edge[0]
        if represent_integer(edge[1]):
            node1 = label_dict[edge[1]]
        else:
            node1 = edge[1]

        fina_adj_list.append([node0, node1, hamming_distance(node0, node1)])
        fina_adj_list.append([node1, node0, hamming_distance(node0, node1)])

    return [fina_adj_list, min_parsimony_score]


with open('E:molecular_evolution/dataset_10335_10.txt', 'r') as f:
    n_leaves = int(f.readline())
    adj_list_test = []
    for row in f.readlines():
        row = row.strip().split('->')
        adj_list_test.append(row)

scores = small_parsimony(adj_list_test)
final_adjlist, min_score = final_tree(adj_list_test, scores)
print(min_score)
for edge in final_adjlist:
    print(str(edge[0]) + '->' + str(edge[1]) + ':' + str(edge[2]))
