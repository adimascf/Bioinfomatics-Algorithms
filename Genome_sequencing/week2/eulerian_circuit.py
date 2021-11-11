from collections import defaultdict
from random import choice


def eulerian_circuit(graph_dict):
    """Searching an eulerian circuit from a given adjacency list in a dictionary. Input dictionary"""
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


def input_solution(arr):
    """Convert a list solution into string with arrows"""
    result = arr[0]
    for item in arr[1:]:
        result += '->' + item
    return result


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba3f.txt', 'r') as file:
        adjacency_list = dict((line.strip().split(' -> ') for line in file))
        for key in adjacency_list:
            adjacency_list[key] = adjacency_list[key].split(',')

    final = eulerian_circuit(adjacency_list)
    print(input_solution(final))


if __name__ == '__main__':
    main()
