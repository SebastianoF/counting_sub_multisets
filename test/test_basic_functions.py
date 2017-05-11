import numpy as np
from nose.tools import assert_equal, assert_true, assert_raises
from numpy.testing import assert_array_equal

from methods.auxiliary import binomial, fact, power_lists


def test_binomial_with_tartaglia_triangle():

    def tartaglia_matrix(d):
        m = np.zeros([d, d])
        m[:, 0] = np.ones(d)
        for r in range(1, d):
            for c in range(1, d):
                m[r, c] = m[r-1, c-1] + m[r-1, c]
        return m

    l = 10
    m1 = np.ones([l, l])
    m2 = tartaglia_matrix(l)

    for rr in range(l):
        for cc in range(l):
            m1[rr, cc] = binomial(rr, cc)

    assert_array_equal(m1, m2)


def test_binomial_negative_values():

    assert_equal(binomial(3, 2), 3)
    assert_equal(binomial(3, -2), 0)
    assert_equal(binomial(-3, 2), 0)
    assert_equal(binomial(-3, -2), 0)
    assert_equal(binomial(2, 3), 0)


def test_fact_simple():
    a = [fact(-1), fact(0), fact(1), fact(2), fact(3), fact(4), fact(5)]
    assert_array_equal(a, [0., 1., 1., 2., 6., 24., 120.])


def test_power_set_simple(verbose=True):

    s1 = ['a', 'b', 'c']
    ans_ground = [[], ['a'], ['b'], ['c'], ['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    ans = power_lists(s1)

    if verbose:
        print('')
        print('Power set of ' + str(s1) + ':')
        print(ans)

    assert_equal(len(ans), len(ans_ground))
    for i in range(len(ans)):
        assert_true(ans[i] in ans_ground)
