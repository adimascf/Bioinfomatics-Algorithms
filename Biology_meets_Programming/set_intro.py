def set_operation(set_a, set_b, n):
    universe = {i + 1 for i in range(n)}

    # Union
    union = set_a.union(set_b)
    print(union)

    # Intersection
    intersection = set_a.intersection(set_b)
    print(intersection)

    # Set difference
    difference_a = set_a.difference(set_b)
    print(difference_a)
    difference_b = set_b.difference(set_a)
    print(difference_b)

    # Set complement
    complement_a = universe.difference(set_a)
    print(complement_a)
    complement_b = universe.difference(set_b)
    print(complement_b)

    return 'Set common operations'


with open('E:rosalind/rosalind_seto.txt', 'r') as f:
    n_test = int(f.readline().strip())
    seta_test = f.readline().rstrip('\n').lstrip('{').rstrip('}').split(', ')
    setb_test = f.readline().rstrip('\n').lstrip('{').rstrip('}').split(', ')
    seta_test = set(map(lambda x: int(x), seta_test))
    setb_test = set(map(lambda x: int(x), setb_test))
print(set_operation(seta_test, setb_test, n_test))