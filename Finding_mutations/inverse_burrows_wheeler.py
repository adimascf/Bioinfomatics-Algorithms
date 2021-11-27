def invers_bwt(text):
    """Get original text that is produced from BWT.
    input paramter is string of text, returns a string"""
    base_count = {'A': 0, 'C': 0, 'T': 0, 'G': 0, '$': 0}
    text_count = []
    for b in text:
        base_count[b] += 1
        text_count.append((b, base_count[b]))
    sorted_text_count = sorted(text_count)
    result_text = ''
    base = ('$', 1)
    while len(result_text) != len(text):
        temp = text_count.index(base)
        base = sorted_text_count[temp]
        result_text += base[0]
    return result_text


with open('E:finding_mutations/dataset_299_10.txt', 'r') as f:
    genome_test = f.read().strip()
    print(invers_bwt(genome_test))
