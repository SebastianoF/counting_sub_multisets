"""
Construction of all of the possible k-resolution of n:
------------------------------------------------------
Following methods provide all of the possible vectors of length k whose elements are the
integers between 1 and n.
Every step is recursive and glues to all of the possible tails, all the possible heads.
The set of the initial heads is defined as the list [[1],[2],[3] , ... ,[n]].
Tails' set grows every step getting glued with all the heads.
"""


def recurs_all(tails, heads, k):
    """
    recursive constructor of tails and heads
    """
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
    """
    Cut from recurs_all(N, N, k) all the vector whose sum is not n.
    ... ok, maybe there is a best way to do it...!
    :param n: non-negative integer.
    :param k: non-negative integer.
    :return: list of all of the k resolutions of n.
    """
    l = [[j] for j in range(0, n + 1)]
    ans = recurs_all(l, l, k)
    return [ans[i] for i in range(len(ans)) if sum(ans[i]) == n]
