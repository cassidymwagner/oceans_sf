from unittest import TestCase

import numpy as np
import pytest

from oceans_sf.calculate_structure_function_1d import calculate_structure_function_1d


@pytest.mark.parametrize(
    "u, v, sep_id, scalar, traditional_type, boundary, expected_result",
    [
        # Test 1: all traditional structure functions
        (
            np.array([1, 2, 3, 4]),  # u
            np.array([2, 4, 6, 8]),  # v
            1,  # sep_id
            np.array([3, 6, 9, 12]),  # scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            None,  # boundary
            {
                "SF_LL": 1,
                "SF_LLL": -1,
                "SF_LTT": -4,
                "SF_LSS": -9,
            },
            # expected_result
        ),
        # Test 2: all traditional structure functions and periodic boundary
        (
            np.array([1, 2, 3, 2]),  # u
            np.array([2, 4, 6, 4]),  # v
            1,  # sep_id
            np.array([3, 6, 9, 6]),  # scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            "Periodic",  # boundary
            {
                "SF_LL": 1,
                "SF_LLL": 0,
                "SF_LTT": 0,
                "SF_LSS": 0,
            },
            # expected_result
        ),
    ],
)
def test_calculate_structure_function_1d_parameterized(
    u, v, sep_id, scalar, traditional_type, boundary, expected_result
):
    output_dict = calculate_structure_function_1d(
        u, v, sep_id, scalar, traditional_type, boundary
    )

    TestCase().assertDictEqual(output_dict, expected_result)
