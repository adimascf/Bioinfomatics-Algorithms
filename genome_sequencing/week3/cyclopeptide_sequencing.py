from collections import defaultdict

with open('E://problem_dna_sequencing//integer_mass_table.txt', 'r') as f:
    contents = f.readlines()
    table_mass = defaultdict(int)
    amino_acids = []
    for aa in contents:
        a, mass = aa.strip().split(' ')
        table_mass[a] = int(mass)
        amino_acids.append(a)

aa_list = table_mass.keys()


def line_spectrum(peptides, aa_mass):
    prefix_mass = [0]
    for aa in peptides:
        prefix_mass.append(prefix_mass[-1] + int(aa_mass[aa]))

    linier_spectrum = [0]
    for i in range(0, len(prefix_mass)-1):
        for j in range(i+1, len(prefix_mass)):
            linier_spectrum.append(prefix_mass[j]-prefix_mass[i])
    return sorted(linier_spectrum)


def cyclic_spectrum(peptides, aa_mass):
    """Generating each of mass from cyclospectrume(peptide). Input string of peptides and table of mass of amino acids"""
    prefix_mass = [0]
    for aa in peptides:
        prefix_mass.append(prefix_mass[-1] + int(aa_mass[aa]))
    total_mass = prefix_mass[-1]

    cyclic_spectrum = [0]
    for i in range(0, len(prefix_mass)-1):
        for j in range(i+1, len(prefix_mass)):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptides):
                m = total_mass - (prefix_mass[j] - prefix_mass[i])
                cyclic_spectrum.append(m)
    return sorted(cyclic_spectrum)


def tes_cyclic(peptide):
    a = []
    for pep in peptide:
        a.append(table_mass[pep])
    return a


def expand(peptides, expansion_set=aa_list):
    expanded_peptides = []
    for peptide in peptides:
        for aa in expansion_set:
            new_peptide = peptide + aa
            expanded_peptides.append(new_peptide)
    return expanded_peptides


def mass(peptide):
    m = 0
    for pep in peptide:
        m += table_mass[pep]
    return m


def parent_mass(spectrum):
    return spectrum[-1]


def inconsistent(peptide, spectrum):
    a = line_spectrum(peptide, table_mass)
    s = spectrum[:]
    for pep in a:
        if pep not in s:
            return True
        s.remove(pep)
    return False


def spectrify(p):
    a = []
    for c in p:
        t = table_mass[c]
        a.append(t)
    return a


def remove_dupes(l):
    s = []
    for i in l:
        if i not in s:
            s.append(i)
    return s


def cyclopeptide_sequencing(spectrum):
    peptides = [""]
    ans = []
    es = []
    for p in expand(peptides):
        if not inconsistent(p, spectrum):
            es.append(p)

    while peptides:
        peptides = expand(peptides, es)
        for p in peptides[:]:
            if mass(p) == parent_mass(spectrum):
                if cyclic_spectrum(p, table_mass) == spectrum:
                    temp = spectrify(p)
                    ans.append(temp)
                peptides.remove(p)
            elif inconsistent(p, spectrum):
                peptides.remove(p)

    ans = remove_dupes(ans)
    return ans

def main():
    with open('E://rosalind//rosalind_ba4e.txt', 'r') as f:
        contents = f.read().strip()
        spectrum_test = []
        for m in contents.split(' '):
            spectrum_test.append(int(m))

    testing = [0, 113, 128, 186, 241, 299, 314, 427]
    for m in cyclopeptide_sequencing(spectrum_test):
        result = str(m[0])
        for n in m[1:]:
            result += '-' + str(n)
        print(result, end=' ')

if __name__ == '__main__':
    main()
