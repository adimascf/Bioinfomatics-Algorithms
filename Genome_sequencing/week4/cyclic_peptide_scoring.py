from collections import Counter
from collections import defaultdict

with open('E://problem_dna_sequencing//integer_mass_table.txt', 'r') as f:
    contents = f.readlines()
    table_mass = defaultdict(int)
    amino_acids = []
    for aa in contents:
        a, mass = aa.strip().split(' ')
        table_mass[a] = int(mass)
        amino_acids.append(a)


def cyclic_spectrum(peptides):
    """Generating each of mass from cyclospectrume(peptide). Input string of peptides and table of mass of amino acids"""
    prefix_mass = [0]
    for aa in peptides:
        prefix_mass.append(prefix_mass[-1] + int(table_mass[aa]))
    total_mass = prefix_mass[-1]

    cyclic_spectrum = [0]
    for i in range(0, len(prefix_mass)-1):
        for j in range(i+1, len(prefix_mass)):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptides):
                m = total_mass - (prefix_mass[j] - prefix_mass[i])
                cyclic_spectrum.append(m)
    return sorted(cyclic_spectrum)


def theoretical_mass(peptide):
    peptide_dict = Counter(cyclic_spectrum(peptide))
    return peptide_dict


def experimental_mass(spectrum):
    spectrum_dict = Counter(spectrum)
    return spectrum_dict


def circular_scoring(peptides, spectrum):
    """Compute the Score of a Cyclic Peptide Against a Spectrum"""

    peptide_dict = theoretical_mass(peptides)
    spectrum_dict = experimental_mass(spectrum)
    theoretical = list(peptide_dict.keys())
    experimental = list(spectrum_dict.keys())
    score = 0
    for mass in theoretical:
        if mass in experimental:
            score += min(peptide_dict[mass], spectrum_dict[mass])

    return score


with open('E://rosalind//rosalind_ba4f.txt', 'r') as f:
    pep = f.readline().strip('\n')
    s = f.read().strip()
    spec = []
    for m in s.split(' '):
        spec.append(int(m))

print(circular_scoring(pep, spec))
