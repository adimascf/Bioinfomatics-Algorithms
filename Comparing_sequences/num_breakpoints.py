with open('E://rosalind//rosalind_ba6b.txt', 'r') as f:
    contents = f.read()[1:-2].strip()
    contents = contents.split(' ')
    contents = list(map(lambda x: int(x), contents))


def num_breakpoint(perm):
    """counting number of breakpoint in a given permutation array"""
    num = 0
    perm = [0] + perm
    for i in range(1, len(perm)):
        if perm[i] - perm[i-1] != 1:
            num += 1
    return num


print(num_breakpoint(contents))
