def string_from_gapped_patterns(rp_list, k, d):
    """Assemble genome from pair end kmers that already in the path of eulerian"""
    read_1 = ''
    read_2 = ''
    for item in rp_list[:-1]:
        read_1 += item[0][0]
        read_2 += item[1][0]
    read_1 += rp_list[-1][0]
    read_2 += rp_list[-1][1]

    str_length = (2*int(k)) + int(d) + len(rp_list) - 1
    read_length = len(read_1)
    match_length = str_length - read_length

    if read_1.endswith(read_2[:-match_length]):
        return read_1 + read_2[-match_length:]
    return read_1, read_2

with open('E://rosalind//rosalind_ba3l.txt', 'r') as f:
    l_kmer, distance = f.readline().split(' ')
    pairs = f.readlines()
    pairs_end = []
    for item in pairs:
        pairs_end.append(item.replace('\n', '').split('|'))

print(string_from_gapped_patterns(pairs_end, l_kmer, distance))