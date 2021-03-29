import numpy as np
import pytest
import sys
sys.path.insert(0, '..')
import example_function as ef


def test_example_function():
    ref_array = [0, 1, 4]
    ref_array2 = [0, 0.5, 1]

    test_array, test_array2 = ef.example_function()

    np.testing.assert_array_equal(test_array, ref_array)
    np.testing.assert_array_equal(test_array2, ref_array2)
