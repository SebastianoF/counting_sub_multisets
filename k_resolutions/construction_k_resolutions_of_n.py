"""
Recursive construction of all of the possible k-resolution of n:
"""


def recurs_all(tails, heads, k):

    if k < 1:
        raise IOError
    if k == 1:
        return tails
    else:
        tails_new = []
        for i in range(len(tails)):
            for j in range(len(heads)):
                v_temp = tails[i] + heads[j]
                tails_new = tails_new + [v_temp]
        return recurs_all(tails_new, heads, k - 1)


def k_resolutions_list(n, k):

    l = [[j] for j in range(0, n + 1)]
    ans = recurs_all(l, l, k)
    return [ans[i] for i in range(len(ans)) if sum(ans[i]) == n]
