def suffix_array_construction(text):
    """Create suffix array from a given text.
    Index positon from sorted suffix of thte text.
    Input parameter is a text string, returns array of integer."""
    result = [i for i in range(len(text))]
    return sorted(result, key=lambda x: text[x:])


with open('E:finding_mutations/dataset_310_2.txt', 'r') as f:
    genome_test = f.read().strip()
print(*suffix_array_construction(genome_test))
