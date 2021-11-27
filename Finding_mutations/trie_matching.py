from trie import trie_reconstruction
from collections import defaultdict


def prefix_trie_matching(genome, trie):
    """Given a trie, check whether  any pattern apears in string of genome.
    input paramter are string of genome and a dictioanry of trie.
    Returns pattern"""
    leaves = [w for w in trie.keys() if trie[w] == {}]
    i = 0
    symbol = genome[i]
    v = list(trie.keys())[0]
    pattern = ''
    while True:
        if v in leaves:
            return pattern
        elif symbol in trie[v]:
            pattern += symbol
            i += 1
            v = trie[v][symbol]
            try:
                symbol = genome[i]
            except IndexError:
                continue
        else:
            return "No match found"


def trie_matching(genome, trie):
    """Check multiple patterns from trie whether appears or not in a given string of genome.
    If it appears, it will be stored the pattern and the start position index in the genome.
    Input paramters are a string of genome and a trie.
    Returns a dictionary"""
    result = defaultdict(list)
    i = 0
    while i < len(genome):
        temp = prefix_trie_matching(genome[i:], trie)
        if temp != "No match found":
            result[temp].append(i)
        i += 1
    return result


with open("E:finding_mutations/dataset_294_8.txt", "r") as f:
    genome_test = f.readline().strip()
    pattern_test = f.readline().strip().split(' ')

trie_test = trie_reconstruction(pattern_test)

result = trie_matching(genome_test, trie_test)
for item in result:
    print(str(item)+':', *result[item])
