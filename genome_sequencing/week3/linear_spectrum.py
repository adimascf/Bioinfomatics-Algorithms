from collections import defaultdict

with open('E://problem_dna_sequencing//integer_mass_table.txt', 'r') as f:
    contents = f.readlines()
    table_mass = defaultdict(int)
    amino_acids = []
    for aa in contents:
        a, mass = aa.strip().split(' ')
        table_mass[a] = int(mass)
        amino_acids.append(a)


def line_spectrum(peptides):
    """Generate the Theoretical Spectrum of a Linear Peptide from a given amino acids sequence"""
    prefix_mass = [0]
    for aa in peptides:
        prefix_mass.append(prefix_mass[-1] + int(table_mass[aa]))

    linier_spectrum = [0]
    for i in range(0, len(prefix_mass)-1):
        for j in range(i+1, len(prefix_mass)):
            linier_spectrum.append(prefix_mass[j]-prefix_mass[i])
    return sorted(linier_spectrum)


with open('E://rosalind//rosalind_ba4j.txt') as file:
    peptides_cs = file.read().strip()
result = line_spectrum(peptides_cs)
final = list(map(lambda x: str(x), result))
print(' '.join(final))
