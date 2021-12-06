def burrows_wheeler_tranform(text):
    """Create string that produced from Burrows wheeler Transfrom.
    input paramter is text, returns text string."""

    k = len(text)
    cyclic_rotation = [text[k-i:k] + text[:k-i] for i in range(k)]
    matrix_bw = sorted(cyclic_rotation)
    result = ''
    for row in matrix_bw:
        result += row[-1]
    return result


with open('E:finding_mutations/dataset_297_5.txt', 'r') as f:
    genome_test = f.read().strip()

# print(burrows_wheeler_tranform(genome_test))
