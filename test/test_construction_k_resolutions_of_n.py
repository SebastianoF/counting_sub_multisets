from nose.tools import assert_equal, assert_true, assert_raises
from numpy.testing import assert_array_equal
from aux_functions.construction_k_resolutions_of_n import k_resolutions_list


def test_k_resolutions_list_simple():
    ans_ground = [[0, 0, 4], [0, 1, 3], [0, 2, 2], [0, 3, 1], 
                  [0, 4, 0], [1, 0, 3], [1, 1, 2], [1, 2, 1], 
                  [1, 3, 0], [2, 0, 2], [2, 1, 1], [2, 2, 0],  
                  [3, 0, 1], [3, 1, 0], [4, 0, 0]]
    ans = k_resolutions_list(4, 3)

    assert_equal(len(ans), len(ans_ground))
    for i in range(len(ans)):
        assert_true(ans[i] in ans_ground)


def test_k_resolutions_list_extreme():
    with assert_raises(IOError):
        k_resolutions_list(5, 0)


def test_k_resolutions_list_extreme_1():
    ans_ground = [[1]]
    ans = k_resolutions_list(1, 1)
    assert_array_equal(ans, ans_ground)



