from collections import defaultdict


def trie_reconstruction(patterns):

    trie = defaultdict(dict)

    for pat in patterns:
        current_node = 0
        for i in range(len(pat)):
            current_symbol = pat[i]
            if current_symbol in trie[current_node]:
                current_node = trie[current_node][current_symbol]
            else:
                node = len(trie)
                trie[current_node][current_symbol] = node
                trie[node] = {}
                current_node = node

    return trie


# with open("E:finding_mutations/dataset_294_4.txt", "r") as f:
#     patterns_test = f.read().strip().split(' ')

# result = []
# for key, val in trie_reconstruction(patterns_test).items():
#     for k, v in val.items():
#         result.append([key, v, k])

# result = sorted(result, key=lambda x: x[1])
# for i in result:
#     print(*i)
