from collections import defaultdict
from collections import Counter


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


def theoretical_mass_linier(peptide):
    peptide_dict = Counter(line_spectrum(peptide))
    return peptide_dict


def experimental_mass(spectrum):
    spectrum_dict = Counter(spectrum)
    return spectrum_dict


def linier_scoring(peptides, spectrum):
    peptide_dict = theoretical_mass_linier(peptides)
    spectrum_dict = experimental_mass(spectrum)
    theoretical = list(peptide_dict.keys())
    experimental = list(spectrum_dict.keys())
    score = 0
    for mass in theoretical:
        if mass in experimental:
            score += min(peptide_dict[mass], spectrum_dict[mass])
    return score


def trim(leaderboard, spectrum, N):
    pep_score = defaultdict(int)
    l_score = []
    for j in range(len(leaderboard)):
        peptide = leaderboard[j]
        pep_score[peptide] = linier_scoring(peptide, spectrum)
        l_score.append(linier_scoring(peptide, spectrum))
    l_score = list(reversed(sorted(l_score)))
    pep_score = sorted(pep_score, key=pep_score.get, reverse=True)

    m = linier_scoring(pep_score[N-1], spectrum)
    for j in range(N, len(pep_score)):
        if linier_scoring(pep_score[j], spectrum) < m:
            return ' '.join(pep_score[:j])
    return ' '.join(pep_score)

def main():
    with open('E://rosalind//rosalind_ba4l.txt', 'r') as f:
        leaderboard_test = f.readline().split(' ')
        spectrum_test0 = f.read().strip()
        N_test = int(spectrum_test0[-1])
        specs = []
        for i in spectrum_test0.split(' ')[:-1]:
            specs.append(int(i))
        print(trim(leaderboard_test, specs, N_test))


if __name__ == '__main__':
    main()
