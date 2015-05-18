def fill_gap_method_simple(original_series, reference_series):
    '''Fernando...'''
    import numpy as np
    import pandas as pd
    ##
    # Boolean vector with missing values in original series
    missing_bool = np.isnan(original_series)
    return original_series.combine_first(reference_series[missing_bool])
