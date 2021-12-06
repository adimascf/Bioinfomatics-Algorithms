from collections import defaultdict
from HHM_profile_construction_pseudocount import output_format


def hmm_parameters_estimation(emssion_string, hidden_path, emission_symbols, state_symbols):
    """Creates parameters estimation of HMM, transition matrix and emission matrix
    based on emission string and hidden path string.
    Return transition matrix and emission matrix in dictionary."""

    num_transition = defaultdict(dict)
    for state1 in state_symbols:
        for state2 in state_symbols:
            num_transition[state1][state2] = 0

    for i in range(len(hidden_path)-1):
        state1 = hidden_path[i]
        state2 = hidden_path[i+1]
        num_transition[state1][state2] += 1

    transition_matrix = defaultdict(dict)

    for state1, val in num_transition.items():
        total = sum(list(val.values()))

        if total == 0:
            for state2, v in val.items():
                transition_matrix[state1][state2] = 1/len(state_symbols)
        else:
            for state2, v in val.items():
                transition_matrix[state1][state2] = v/total

    num_emission = defaultdict(dict)
    for state in state_symbols:
        for emission in emission_symbols:
            num_emission[state][emission] = 0

    i = 0
    while i < len(emssion_string):
        state = hidden_path[i]
        emission = emssion_string[i]
        num_emission[state][emission] += 1
        i += 1

    emission_matrix = defaultdict(dict)
    for state, val in num_emission.items():
        total = sum(list(val.values()))

        if total == 0:
            for symbol, v in val.items():
                emission_matrix[state][symbol] = 1/len(emission_symbols)
        else:
            for symbol, v in val.items():
                emission_matrix[state][symbol] = v/total

    return transition_matrix, emission_matrix


with open('E:finding_mutations/dataset_26260_4.txt', 'r') as f:
    emission_string_test = f.readline().strip()
    f.readline()
    emission_symbols_test = f.readline().strip().split(' ')
    f.readline()
    hidden_path_test = f.readline().strip()
    f.readline()
    state_symbols_test = f.readline().strip().split(' ')

# trans, emis = hmm_parameters_estimation(emission_string_test,
#                                         hidden_path_test, emission_symbols_test, state_symbols_test)

# print(output_format(trans, emis))
