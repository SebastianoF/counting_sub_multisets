from aux_functions.basic_functions import binomial, power_lists


"""
Closed form computations of k-resolutions with no, upper and lower constraints
-------------------------------------------------------------------------------
Cardinality of k-resolutions are provided with the closed formula developed in the pdf document.
They will be compared with the length of the lists provided by the previous enumerative methods.
"""


def number_of_k_resolutions_n(n, k):
    """
    R_{k}^{n}
    k resolution of n with no constraints, starting from 0
    :param n,k: integer indexes
    :return: number of k-resolutions of n whose elements can include zero
    """
    return binomial(n + k - 1, k - 1)


def number_of_k_resolutions_upper_constraints_wrong(n, t_up):
    """
    k resolutions with uphill constraint, wrong version, examined at the end of section 3.
    :param n: number of element extracted
    :param t_up: constraints uphill vector
    :return:
    """
    return binomial(n - sum(t_up) + len(t_up) - 1, len(t_up) - 1)


def number_of_k_resolutions_lower_constraints(n, low_t):
    """
    $R_{(a_1,a_2, \dots , a_k )^{\downarrow} }^{n}$
    k resolutions with lower constraint
    :param n:
    :param low_t: vector of non-negative integers $(a_1,a_2, \dots , a_k)$ representing lower constraints
    :return: number of k-resolution with lower constraints.
    """
    return binomial(n - sum(low_t) + len(low_t)  - 1, len(low_t) - 1)


def number_of_k_resolutions_upper_constraints(n, up_t, verbose=False):
    """
    Fatti non foste a computare come bruti.
    $R_{(a_1,a_2, \dots , a_k )^{\uparrow} }^{n}$
    :param n: positive integer
    :param up_t: vector of non-negative integers $(a_1,a_2, \dots , a_k)$ representing upper constraints
    :return:  $\binom{n+k-1}{k-1} - \sum_{m=1}^{k} (-1)^{m+1}
    \sum_{1\leq i_1 < i_2 < \dots <i_m \leq  k}
    \binom{n-\sum_{l=1}^{m} a_{i_{l}} - m + k - 1}{k-1}$
    """

    k = len(up_t)
    p = power_lists(range(1, k + 1))

    s = 0
    for l in p:
        s += ((-1)**(len(l))) * binomial(n + k - 1 - len(l) - sum([up_t[i - 1] for i in l]), k - 1)

    if verbose:
        print p
        print 'emmenems of each color in the pocket : ' + str(up_t)
        print 'emmenems in the hand : ' + str(n)
        print 'numbers of handfuls : ' + str(s)

    return s
