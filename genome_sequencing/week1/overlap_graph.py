def overlap_graph(arr_mers):
    prefix = len(arr_mers[0])-1
    graph_dict = {}
    for mer in sorted(arr_mers):
        graph_dict[mer] = []
    for key in graph_dict.keys():
        for mer in arr_mers:
            if key.endswith(mer[:prefix]):
                graph_dict[key].append(mer)
    filtering = dict((key, val)
                     for key, val in graph_dict.items() if val != [])
    return filtering


def format_arrow(dictionary_result):
    for k, v in dictionary_result.items():
        print(k + ' -> ' + ','.join(v))


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba3c.txt') as f:
        contents = [line.strip() for line in f.readlines()]

    result = overlap_graph(contents)
    format_arrow(result)


if __name__ == '__main__':
    main()
