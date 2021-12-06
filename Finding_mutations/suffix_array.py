def suffix_array_construction(text):
    """Create suffix array from a given text.
    Index positon from sorted suffix of thte text.
    Input parameter is a text string, returns array of integer."""
    result = [i for i in range(len(text))]
    return sorted(result, key=lambda x: text[x:])


def partial_suffix_array(text, k):
    """Eliminate the values that can't be divisible by integer k.
    input paramaters are text, suffix array (list), and integer k.
    returns a dictionary of indexes and the values of suffix array."""
    suffix_arr = suffix_array_construction(text)
    result = {}
    for i in range(len(suffix_arr)):
        if suffix_arr[i] % k == 0:
            result[i] = suffix_arr[i]
    return result


# with open('E:finding_mutations/dataset_9809_2.txt', 'r') as f:
#     genome_test = f.readline().strip()
#     k_test = int(f.readline().strip())
# partial = partial_suffix_array(genome_test, k_test)
# print(partial)
