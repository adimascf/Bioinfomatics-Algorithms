from collections import defaultdict


def modified_suffix_trie(genome):

    trie = defaultdict(dict)
    for i in range(len(genome)):
        current_node = 0
        for j in range(i, len(genome)):
            current_symbol = genome[j]
            if current_symbol in trie[current_node]:
                current_node = trie[current_node][current_symbol]
            else:
                node = len(trie)
                trie[node] = {}
                trie[current_node][current_symbol] = node
                current_node = node

        # if trie[current_node] == {}:
        #     trie[current_node] = str(i)

    return trie


def get_key(dictionary):

    result = []
    for k, v in dictionary.items():
        result.append(k)
    return result


def modified_suffix_tree_construction(genome):

    trie = modified_suffix_trie(genome)
    current = 0
    paths = []
    marked = []
    while current < len(trie):
        temp0 = trie[current]
        for i in get_key(temp0):
            path = ''
            path += i
            temp1 = trie[current][i]
            if temp1 not in marked:
                while len(trie[temp1]) == 1:
                    path += get_key(trie[temp1])[0]
                    marked.append(temp1)
                    temp1 = trie[temp1][path[-1]]
            paths.append(path)
        current += 1
        while current in marked:
            current += 1
    return paths


print(modified_suffix_tree_construction("ATAAATG$"))
