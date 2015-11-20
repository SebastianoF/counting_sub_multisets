"""
Construction of all of the possible k-resolution of n with upper constraints:
----------------------------------------------------------------------------
Following methods provide the list of all of the k-resolutions of n with upper constraints
defined by the list t_up = (a_1, a_2, ..., a_k)
"""


def recurs_upper_constraints(tails, heads, k, t_up):

    if k == 0:
        return tails
    else:
        tails_new = []
        for b in range(len(tails)):
            for p in range(len(heads)):
                if heads[p][0] <= t_up[len(tails[0])]:
                    v_temp = tails[b] + heads[p]
                    tails_new = tails_new + [v_temp]
        return recurs_upper_constraints(tails_new, heads, k - 1, t_up)


def all_vectors_upper_constraints(n, k, t_up):

    if k == len(t_up):
        heads_starters = []
        for i in range(0, n + 1):
            heads_starters = heads_starters + [[i]]
        ans = recurs_upper_constraints([[]], heads_starters, k, t_up)
        return ans
    else:
        print 'input : (n, k, t), list t must have dim = k'


def k_resolutions_upper_constraints_list(n, t_up):
    """
    Computation of the list of the k-resolution of n with upper constraint
    given by the vector T
    :param n:
    :param t_up:
    :return:
    """
    l = all_vectors_upper_constraints(n, len(t_up), t_up)
    return [l[i] for i in range(len(l)) if sum(l[i]) == n]

