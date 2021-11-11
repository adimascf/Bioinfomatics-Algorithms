from random import choice
from itertools import product
from collections import defaultdict


def eulerian_circuit(graph_dict):
    """Searching an eulerian circuit"""
    stack = []
    circuit = []
    stack.append(choice([item[0] for item in graph_dict.values()]))
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
                        circuit.append(stack[-1])
                        del stack[-1]
    return circuit[::-1]


def construct_binary_strings(k):
    """generates binary strings from a given length of kmer(integer). Input integer and return a list"""
    return ["".join(i) for i in product('01', repeat=k)]


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


def path_to_string(arr):
    result = arr[0]
    for item in arr[1:]:
        result += item[-1]
    return result


def k_uni_circular_problem(k):
    """Reconstructing binary string from any given length. Input as integer and out as string"""
    binary_strings = construct_binary_strings(k)
    db = de_brujin_kmers(binary_strings)
    circuit = eulerian_circuit(db)
    result = path_to_string(circuit)
    # due to this will result a circle so the result is sliced in -(k-1) position
    return result[:-(k-1)]


if __name__ == '__main__':
    print(k_uni_circular_problem(9))
