def outcome_probability(emitted_string, hidden_path, emission_matrix):
    """Calculates the probability that an HMM will emit a string given its hidden path.
    Input paramters are emited string, hidden path string, and dictionary of emission matrix.
    Return floating number of probability."""

    path_length = len(emitted_string)
    probability = 1
    i = 0
    while i < path_length:
        probability *= emission_matrix[hidden_path[i] + emitted_string[i]]
        i += 1
    return probability


with open('E:rosalind/rosalind_ba10b.txt', 'r') as f:
    content = f.read().strip().split('--------')
    emission_outcome_test = content[0].strip()
    emissions_test = content[1].strip().split('\t')
    hidden_path_test = content[2].strip()
    states_test = content[3].strip().split('\t')
    temp = content[4].strip().split('\n')
    temp1 = temp[0].split('\t')
    emission_matrix_test = {}
    for i in range(len(states_test)):
        for j in range(len(emissions_test)):
            emission_matrix_test[states_test[i] + emissions_test[j]] = float(
                temp[i + 1].split('\t')[j + 1])
print(
    outcome_probability(emission_outcome_test, hidden_path_test,
                        emission_matrix_test))
