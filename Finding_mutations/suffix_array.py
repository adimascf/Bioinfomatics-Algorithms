def suffix_array_construction(text):

    result = [i for i in range(len(text))]
    return sorted(result, key=lambda x: text[x:])


with open('E:finding_mutations/dataset_310_2.txt', 'r') as f:
    genome_test = f.read().strip()
print(*suffix_array_construction(genome_test))
