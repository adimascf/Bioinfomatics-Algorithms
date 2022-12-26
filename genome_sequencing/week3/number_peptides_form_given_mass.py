# Using recursive method, this is very comlicated!
aa_mass = {57: 'G', 71: 'A', 87: 'S', 97: 'P',
           99: 'V', 101: 'T', 103: 'C', 113: 'I/L',
           114: 'N', 115: 'D', 128: 'K/Q', 129: 'E',
           131: 'M', 137: 'H', 147: 'F', 156: 'R', 163: 'Y', 186: 'W'}


def counting_peptides(mass, mass_list):

    if mass == 0:
        return 1, mass_list
    if mass < 57:
        return 0, mass_list
    if mass in mass_list:
        return mass_list[mass], mass_list

    n = 0
    for i in aa_mass:
        k, mass_list = counting_peptides(mass-i, mass_list)

        n += k
    mass_list[mass] = n
    return n, mass_list

with open('E://rosalind//rosalind_ba4d.txt', 'r') as f:
    mass = f.read().strip()
    mass = int(mass)

print(counting_peptides(mass, {})[0])