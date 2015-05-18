def fill_gap_method_regress(reg_params, original_series, reference_series):
    '''Fernando...'''
    import numpy as np
    import pandas as pd
    ##
    # Boolean vector with missing values in original series
    missing_bool = np.isnan(original_series)
    #
    # Compute missing data using regression results. Note the parameter order. (param 0 slope 1 constant term) 
    predicted_data = reference_series[missing_bool]*reg_params[0] + reg_params[1]
    #
    return original_series.combine_first(predicted_data)
