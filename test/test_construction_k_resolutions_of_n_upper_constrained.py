from numpy.testing import assert_equal

from k_resolutions.construction_k_resolutions_of_n_upper_constrained import k_resolutions_upper_constraints_list


def test_k_resolutions_lower_constraints_list_simple():
    ans_ground = [[0, 1, 3], [0, 2, 2], [1, 0, 3], [1, 1, 2], [1, 2, 1]]
    ans = k_resolutions_upper_constraints_list(4, [1, 2, 3])

    assert_equal(len(ans), len(ans_ground))
    for a in ans:
        assert a in ans_ground


def test_k_resolutions_lower_constraints_list_simple_1():
    ans_ground = [[0, 2, 3, 1], [1, 1, 3, 1], [1, 2, 2, 1], [1, 2, 3, 0]]
    ans = k_resolutions_upper_constraints_list(6, [1, 2, 3, 1])

    assert_equal(len(ans), len(ans_ground))
    for a in ans:
        assert a in ans_ground


def test_k_resolutions_lower_constraints_list_simple_2():
    ans_ground = [[3, 7], [4, 6], [5, 5], [6, 4], [7, 3]]
    ans = k_resolutions_upper_constraints_list(10, [7, 7])

    assert_equal(len(ans), len(ans_ground))
    for a in ans:
        assert a in ans_ground


def test_k_resolutions_lower_constraints_list_simple_extreme():
    ans_ground = []
    ans = k_resolutions_upper_constraints_list(4, [1, 2])

    assert_equal(len(ans), len(ans_ground))
