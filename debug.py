import numpy as np

import parameter_analysis

def check_for_nan(array):
    """Check for NaN locations within an array."""
    nan_locations = []
    number = 0
    for value in array:
        if np.isnan(value):
            nan_locations.append(number)
            number += 1
    return nan_locations
    # Should return empty list if input is valid
