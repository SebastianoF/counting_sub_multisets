from numpy.testing import assert_equal

from k_resolutions.construction_k_resolutions_of_n_lower_constrained import k_resolutions_lower_constraints_list


def test_k_resolutions_lower_constraints_list_simple():
    ans_ground = [[1, 3], [2, 2]]
    ans = k_resolutions_lower_constraints_list(4, [1, 2])

    assert_equal(len(ans), len(ans_ground))
    for a in ans:
        assert a in ans_ground


def test_k_resolutions_lower_constraints_list_simple_1():
    ans_ground = [[1, 2, 3]]
    ans = k_resolutions_lower_constraints_list(6, [1, 2, 3])

    assert_equal(len(ans), len(ans_ground))


def test_k_resolutions_lower_constraints_list_simple_2():
    ans_ground = [[1, 2, 7], [1, 3, 6], [1, 4, 5], [1, 5, 4], [1, 6, 3], 
                  [2, 2, 6], [2, 3, 5], [2, 4, 4], [2, 5, 3], [3, 2, 5], 
                  [3, 3, 4], [3, 4, 3], [4, 2, 4], [4, 3, 3], [5, 2, 3]]
    ans = k_resolutions_lower_constraints_list(10, [1, 2, 3])

    assert_equal(len(ans), len(ans_ground))
    for a in ans:
        assert a in ans_ground


def test_k_resolutions_lower_constraints_list_simple_extreme():
    ans_ground = []
    ans = k_resolutions_lower_constraints_list(4, [1, 2, 3])

    assert_equal(len(ans), len(ans_ground))
