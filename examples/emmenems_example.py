from methods.construction_k_resolutions_of_n_upper_constrained import k_resolutions_upper_constraints_list
from methods.counting_k_resolutions_closed_forms import number_of_k_resolutions_upper_constraints


if __name__ == "__main__":
    """
    An example of counting sub-multisets of fixed cardinality of a given multiset using the 
    M&Ms pocket example.
    """

    # Example 1

    msg_1 = 'Given a pocket of 10 M&Ms, divided in the 6 classical colours ' \
            '3 red, 2 orange , 1 yellow, 4 blue, 3 brown and 3 green, how ' \
            'many different handful of 7 ' \
            'candies can we extract?'

    n_1 = 7
    t_up1 = [3, 2, 1, 4, 3, 3]

    answer_1 = number_of_k_resolutions_upper_constraints(n_1, t_up1)

    print('')
    print(msg_1)
    print('Answer: ' + str(answer_1))
    print('Do you want to visualize them all (They are computed by brute force)?')
    see_them = input('(y/n):')

    if see_them.lower() == 'y':
        list_1 = k_resolutions_upper_constraints_list(n_1, t_up1)
        print('Possible handfuls: ' + str(list_1) + '\n')

    # Example 2

    msg_2 = 'Given a pocket of 30 M&Ms, divided in the 6 classical colours' \
            '11 red, 9 orange , 6 yellow, 14 blue, 3 brown and 17 green, how many '\
            'different handful of 12 candies can we extract?'

    n_2 = 12
    t_up2 = [11, 9, 6, 14, 3, 17]

    answer_2 = number_of_k_resolutions_upper_constraints(n_2, t_up2)

    print('')
    print(msg_2)
    print('Answer: ' + str(answer_2))
    print('Do you want to visualize them all (They are computed by brute force)?')
    see_them = input('(y/n):')
    if see_them.lower() == 'y':

        i_have_a_lot_of_spare_time = False
        print('ARE YOU SURE?? You must have a lot of spare time!')
        see_them = input('(y/n):')
        if see_them.lower() == 'y':
            i_have_a_lot_of_spare_time = True

        if i_have_a_lot_of_spare_time:
            print('\n\tPlease wait... (press Ctrl+C when you had enough!)')
            list_2 = k_resolutions_upper_constraints_list(n_2, t_up2)
            print('Possible handfuls: ' + str(list_2) + '\n')
        else:
            list_2 = 'no time to wait for this computation at the moment!'
