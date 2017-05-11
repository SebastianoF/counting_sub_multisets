import time

from methods.construction_k_resolutions_of_n import k_resolutions_list
from methods.construction_k_resolutions_of_n_lower_constrained import k_resolutions_lower_constraints_list
from methods.construction_k_resolutions_of_n_upper_constrained import k_resolutions_upper_constraints_list
from methods.counting_k_resolutions_closed_forms import number_of_k_resolutions_upper_constraints, number_of_k_resolutions_n, number_of_k_resolutions_lower_constraints


if __name__ == "__main__":
    # Comparisons between closed form and length of lists of k-resolutions with no, lower or upper constraints.

    #######################
    # k -resolutions of n #
    #######################

    n = 7
    k = 5

    closed_form = number_of_k_resolutions_n(n, k)
    counting_solutions = len(k_resolutions_list(n, k))

    print('\n' + str(k) + '-resolutions of ' + str(n) + ', unconstrained:')
    print('closed form            = ' + str(closed_form))
    print('counting the solutions = ' + str(counting_solutions))
    print('It is ' + str(closed_form == counting_solutions) + ' that closed form equals the direct enumerations. \n')

    #########################################
    # k -resolutions of n lower constraints #
    #########################################

    n_lower = 15
    t_lower = [3, 4, 1, 2]
    k_lower = len(t_lower)

    closed_form = number_of_k_resolutions_lower_constraints(n_lower, t_lower)
    counting_solutions = len(k_resolutions_lower_constraints_list(n_lower, t_lower))

    print('\n' + str(k_lower) + '-resolutions of ' + str(n_lower) + ', with lower constraints ' + str(t_lower) + ':')
    print('closed form            = ' + str(closed_form))
    print('counting the solutions = ' + str(counting_solutions))
    print('It is ' + str(closed_form == counting_solutions) + ' that closed form equals the direct enumerations. \n')

    #########################################
    # k -resolutions of n upper constraints #
    #########################################

    n_upper = 30
    t_upper = [14, 3, 7, 10, 10]  # [4, 3, 1, 5, 5] [5, 7, 8, 5, 4, 2]
    k_upper = len(t_upper)

    time_results = [0.0] * 2

    start = time.time()
    closed_form = number_of_k_resolutions_upper_constraints(n_upper, t_upper)
    time_results[0] += (time.time() - start)

    start = time.time()
    counting_solutions = len(k_resolutions_upper_constraints_list(n_upper, t_upper))
    time_results[1] += (time.time() - start)

    print('\n' + str(k_upper) + '-resolutions of ' + str(n_upper) + ', with upper constraints ' + str(t_upper) + ':')
    print('closed form            = ' + str(closed_form))
    print('counting the solutions = ' + str(counting_solutions))
    print('It is ' + str(closed_form == counting_solutions) + ' that closed form equals the direct enumerations. \n')

    print ('Computational time for upper resolutions constraints: ')
    print ('with closed form: ' + str(time_results[0]) + ' sec.')
    print ('with direct enumeration: ' + str(time_results[1]) + ' sec.')

