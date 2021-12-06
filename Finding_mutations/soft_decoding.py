from collections import defaultdict


def soft_decoding(emission_string, transition_matrix, emission_matrix, emission_symbols, state_symbols):
    """Calcultae outcome likelihood Pr(x)"""

    init_transition_probability = 1/len(state_symbols)
    emission_length = len(emission_string)

    forward_value = defaultdict(dict)
    for i in range(emission_length):
        for current_state in state_symbols:
            if i == 0:
                forward_value[current_state][i] = 1 * \
                    init_transition_probability * \
                    emission_matrix[current_state][emission_string[i]]

            else:
                forward_value[current_state][i] = 0
                for state in state_symbols:
                    forward_value[current_state][i] += forward_value[state][i-1] * \
                        transition_matrix[state][current_state] * \
                        emission_matrix[current_state][emission_string[i]]

    pr_x = 0
    for state in state_symbols:
        pr_x += forward_value[state][emission_length - 1]

    backward_value = defaultdict(dict)
    for i in range(emission_length - 1, -1, -1):
        for current_state in state_symbols:
            if i == emission_length - 1:
                backward_value[current_state][i] = 1

            else:
                backward_value[current_state][i] = 0
                for state in state_symbols:
                    backward_value[current_state][i] += backward_value[state][i+1] \
                        * transition_matrix[current_state][state] * \
                        emission_matrix[state][emission_string[i+1]]

    condition_probability = defaultdict(dict)
    for i in range(emission_length):
        for state in state_symbols:
            condition_probability[state][i] = forward_value[state][i] * \
                backward_value[state][i] / pr_x

    return condition_probability


with open('E:finding_mutations/dataset_26261_5.txt', 'r') as f:
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


result = soft_decoding(emission_string_test, transition_matrix_test, emission_matrix_test,
                       emission_symbols_test, state_symbols_tets)

to_print = '\t\t'.join(state_symbols_tets) + '\n'
for i in range(len(emission_string_test)):
    for state in state_symbols_tets:
        to_print += str(round(result[state][i], 4)).rstrip('0') + '\t'
    to_print += '\n'
print(to_print)
