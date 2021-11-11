from collections import defaultdict


def de_brujin_kmers(arr):
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


def main():
    with open('E://problem_dna_sequencing/rosalind/rosalind_ba3e.txt') as f:
        contents = [line.strip() for line in f.readlines()]

    for k, v in de_brujin_kmers(contents).items():
        print(k + ' -> ' + ','.join(v))


if __name__ == '__main__':
    main()
