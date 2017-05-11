from scipy.misc import factorial
from itertools import chain, combinations


def binomial(n, k):
    """
    Binomial coefficients, thanks to Andrew Dalke.
    """
    if 0 <= k <= n:
        n_tok = 1
        k_tok = 1
        for t in xrange(1, min(k, n - k) + 1):
            n_tok *= n
            k_tok *= t
            n -= 1
        return n_tok // k_tok
    else:
        return 0


def fact(n):
    """
    Wrap the predefined function factorial from scipy.misc
    :param n: integer
    :return: factorial of n type float
    """
    return float(factorial(n, True))


def power_lists(s):
    """
    Returns the power set of the list s, as a list of lists.
    :param s: list of elements.
    :return: power sets of the list s, as collection of all of the possible 'sub-lists' of the input list.
    """
    result = []
    for z in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)):
        result += [list(z)]
    return result
