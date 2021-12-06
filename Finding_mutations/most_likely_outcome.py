from collections import defaultdict


def outcome_likelihood(emission_matrix, transition_matrix, states, emission_string):
    """Calculate the likelihood, the probability that HMM emits emission sequence string.
    Input paramters are emission matrix (dict), transition matrix (dict),
    a list of states, emission sequence in string.
    Returns floating number of likelihood."""

    initial_trans_prob = 1/len(states)
    forward = defaultdict(dict)
    k = len(emission_string)

    for i in range(k):
        for curr_state in states:

            if i == 0:
                forward[curr_state][i] = 1 * initial_trans_prob * \
                    emission_matrix[curr_state + emission_string[i]]

            else:
                forward[curr_state][i] = 0
                for s in states:
                    forward[curr_state][i] += forward[s][i-1] * transition_matrix[s +
                                                                                  curr_state] * emission_matrix[curr_state + emission_string[i]]
    likelihood = 0
    for state in states:
        likelihood += forward[state][k-1]
    return likelihood


with open('E:finding_mutations/dataset_26257_4.txt', 'r') as f:
    content = f.read().strip().split('--------')
    emision_string_test = content[0].strip()
    emission_symbols_test = content[1].strip().split(' ')
    states_test = content[2].strip().split(' ')
    temp0 = content[3].strip().split('\n')
    temp1 = temp0[0].split('\t')
    transition_matrix_test = {}
    for i in range(len(states_test)):
        for j in range(len(states_test)):
            transition_matrix_test[states_test[i] +
                                   states_test[j]] = float(temp0[i+1].split('\t')[j+1])
    temp2 = content[4].strip().split('\n')
    temp3 = temp2[0].split('\t')
    emission_matrix_test = {}
    for i in range(len(states_test)):
        for j in range(len(emission_symbols_test)):
            emission_matrix_test[states_test[i] +
                                 emission_symbols_test[j]] = float(temp2[i+1].split('\t')[j+1])

print(outcome_likelihood(emission_matrix_test,
      transition_matrix_test, states_test, emision_string_test))
