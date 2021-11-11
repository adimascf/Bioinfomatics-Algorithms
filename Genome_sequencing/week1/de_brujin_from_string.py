from collections import defaultdict


def de_brujin_string(k, text):
    n = k - 1
    d = defaultdict(list)
    for i in range(len(text)-n+1):
        d[text[i:i+n]]
    for key in d.keys():
        for j in range(len(text)-k+1):
            if str(key).endswith(text[j:j+k][:-1]):
                d[key].append((text[j+1:j+k]))
    result = dict((key, val) for key, val in d.items() if val != [])
    return result


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba3d.txt') as f:
        len_kmer = f.readline().strip()
        sequence = f.read().strip('\n')

    for key, val in de_brujin_string(int(len_kmer), sequence).items():
        print(key + ' -> ' + ','.join(val))


if __name__ == '__main__':
    main()
