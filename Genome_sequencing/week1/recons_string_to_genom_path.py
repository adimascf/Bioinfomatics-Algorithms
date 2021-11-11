def string_recons(arr_kmer):
    reconstruction = ''
    for i in range(len(arr_kmer)):
        if arr_kmer[i][:-1] not in [kmer[1:] for kmer in arr_kmer]:
            reconstruction = arr_kmer[i]
    arr_kmer.pop(arr_kmer.index(reconstruction))

    for _ in range(len(arr_kmer)):
        for mer in arr_kmer:
            if mer.startswith(reconstruction[-2:]):
                reconstruction += mer[-1]
                arr_kmer.pop(arr_kmer.index(mer))
    return reconstruction


def spelled_genome_path(arr_mers):
    result = arr_mers[0]
    for mer in arr_mers[1:]:
        result += mer[-1]
    return result


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba3b.txt') as f:
        contents = [line.strip() for line in f.readlines()]
    result = spelled_genome_path(contents)
    print(spelled_genome_path(result))


if __name__ == '__main__':
    main()
