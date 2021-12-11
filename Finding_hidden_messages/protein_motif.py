from urllib.request import urlopen

ids_test = []
with open('E:rosalind/rosalind_mprt.txt', 'r') as f:
    content = f.readlines()
    for id in content:
        ids_test.append(id.strip())


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


def get_sequence(ids):
    """Get protein sequence in uniport website as fasta file format and save the file"""

    for id in ids:
        url = 'http://www.uniprot.org/uniprot/' + id + '.fasta'
        data = urlopen(url)
        fasta = data.read().decode('utf-8', 'ignore')
        with open('E:rosalind/protein_sequence.fasta', 'a') as f:
            f.write(fasta)


def find_motif(protein_sequence):
    """Finds start position of N-glycosylation motif (if any) N{P}[ST]{P}
    in the protein sequence.
    Input paramters is protein sequence in string, returns a list of integer."""

    motif_length = 4  # the length of N-glycosylation motif
    motif_positions = []
    for i in range(len(protein_sequence) - motif_length + 1):
        subs_seq = protein_sequence[i:i+4]
        # check if the motif is found
        if subs_seq[0] == 'N' and subs_seq[1] != 'P' and subs_seq[2] in ['S', 'T'] and subs_seq[3] != 'P':
            # output using a index 1 world, so we add 1
            motif_positions.append(i+1)
    return motif_positions


get_sequence(ids_test)
fasta_file = read_fasta('E:rosalind/protein_sequence.fasta')
result = {}
i = 0
for name, seq in fasta_file.items():
    check_motif = find_motif(seq)
    if len(check_motif) > 0:
        print(ids_test[i])
        print(*check_motif)
    i += 1
