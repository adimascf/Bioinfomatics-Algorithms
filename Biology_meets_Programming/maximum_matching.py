from counting_subsets import factorial


def maximum_matching(rna_sequence):

    a = 0
    u = 0
    g = 0
    c = 0

    for base in rna_sequence:
        if base == 'A':
            a += 1
        elif base == 'U':
            u += 1
        elif base == 'G':
            g += 1
        elif base == 'C':
            c += 1

    au = factorial(max(a, u)) // factorial(abs(a - u))
    gc = factorial(max(g, c)) // factorial(abs(g - c))
    return au * gc


with open('E:rosalind/rosalind_mmch.txt', 'r') as f:
    f.readline()
    seq_test = ''
    for seq in f.readlines():
        seq_test += seq.strip()

print(maximum_matching(seq_test))