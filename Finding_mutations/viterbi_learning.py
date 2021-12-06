from collections import defaultdict
from viterbi import decoding_problem
from parameters_estimation import hmm_parameters_estimation
from HHM_profile_construction_pseudocount import output_format


def viterbi_learning(emission_string, initial_transition_matrix, initial_emission_matrix, emission_symbols, state_symbols, num_iter):
    """Implement Viterbi learning for estimating the parameters of an HMM
    Input parameters are emission string, transition matrix (dict), emission matrix (dict),
    emission symbol (list), state symbol (list), number of iteration in integer.
    Returns emission and transition matrix in dictionary after num iteration.
    """

    transition_matrix = initial_transition_matrix
    emission_matrix = initial_emission_matrix

    for _ in range(num_iter):
        # Determines path using current parameters
        hidden_path = decoding_problem(
            emission_matrix, transition_matrix, state_symbols, emission_string)

        # Determines new parameters using hidden path that
        # produced from decoding problem function
        transition_matrix, emission_matrix = hmm_parameters_estimation(
            emission_string, hidden_path, emission_symbols, state_symbols)

    return transition_matrix, emission_matrix


if __name__ == "__main__":

    with open('E:finding_mutations/dataset_26260_8.txt', 'r') as f:
        num_iteration_test = int(f.readline().strip())
        f.readline()
        emission_string_test = f.readline().strip()
        f.readline()
        emission_symbols_test = f.readline().strip().split(' ')
        f.readline()
        state_symbols_tets = f.readline().strip().split(' ')
        f.readline()
        temp = f.read().split('--------')
        temp0, temp1 = temp[0].strip().split('\n'), temp[1].strip().split('\n')
        transition_matrix_test = defaultdict(dict)
        for i in range(len(state_symbols_tets)):
            for j in range(len(state_symbols_tets)):
                transition_matrix_test[state_symbols_tets[i]
                                       ][state_symbols_tets[j]] = float(temp0[i+1].split('\t')[j+1])
        emission_matrix_test = defaultdict(dict)
        for i in range(len(state_symbols_tets)):
            for j in range(len(emission_symbols_test)):
                emission_matrix_test[state_symbols_tets[i]
                                     ][emission_symbols_test[j]] = float(temp1[i+1].split('\t')[j+1])

trans, emis = viterbi_learning(emission_string_test, transition_matrix_test,
                               emission_matrix_test, emission_symbols_test, state_symbols_tets, num_iteration_test)
print(output_format(trans, emis))
