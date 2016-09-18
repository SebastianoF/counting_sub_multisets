"""
Construction of all of the possible k-resolution of n with lower constraints:
----------------------------------------------------------------------------
Following methods provide the list of all of the k-resolutions of n with lower constraints
defined by the list t_low = (a_1, a_2, ..., a_k)
"""


def recurs_lower_constraints(tails, heads, k, t_low):

    if k == 0:
        return tails
    else:
        tails_new = []
        for b in range(len(tails)):
            for p in range(len(heads)):
                if heads[p][0] >= t_low[len(tails[0])]:
                    v_temp = tails[b] + heads[p]
                    tails_new = tails_new + [v_temp]
        return recurs_lower_constraints(tails_new, heads, k - 1, t_low)


def all_vectors_lower_constraints(n, k, t_low):
    if k == len(t_low):
        heads_starter = []
        for i in range(0, n + 1):
            heads_starter = heads_starter + [[i]]
        ans = recurs_lower_constraints([[]], heads_starter, k, t_low)
        return ans
    else:
        raise TypeError('input : (n, k, t), list t must have dim = k')


def k_resolutions_lower_constraints_list(n, t_low):
    l = all_vectors_lower_constraints(n, len(t_low), t_low)
    return [l[i] for i in range(len(l)) if sum(l[i]) == n]
