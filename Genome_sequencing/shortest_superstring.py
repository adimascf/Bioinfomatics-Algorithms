def read_fasta(file_path):
    '''Reading fasta formatted file and returning into line'''
    with open(file_path, 'r') as f:
        # for storing the contents of the file into a list
        fasta_file = [line.strip('\n') for line in f.readlines()]

    # for storing labels and data
    fasta_dict = {}
    fasta_label = ''

    # for preparing data and taking into dictionary
    for line in fasta_file:
        if '>' in line:
            fasta_label = line
            fasta_dict[fasta_label] = ''
        else:
            fasta_dict[fasta_label] += line
    return fasta_dict


def read_assembly(reads_list):
    """Returns a shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome)"""

    result = reads_list[0]
    k = len(reads_list)
    j = 0
    while j < k:
        for i in range(k):
            temp_seq = reads_list[i]
            l = len(temp_seq)

            for start in range(l // 2):
                end = l - start

                if result.startswith(temp_seq[start:]):
                    result = temp_seq[:start] + result

                if result.endswith(temp_seq[:end]):
                    result = result + temp_seq[end:]
        j += 1
    return result


# read_dict = read_fasta('E:problem_dna_sequencing/assembly.txt')
# reads_test = list(read_dict.values())
# print(read_assembly(reads_test))
