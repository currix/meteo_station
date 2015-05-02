def quality_control(datafile, data_format = "CCEE"):
    ''' Docstring...Fernando'''
    ##
    import numpy as np
    import pandas as pd
    ##
    from defined_functions import read_CCEE_data, read_MONT_data, prep_time_series, repvals, check_tinverval, del_rep_values_metdata
    #
    print data_format
    assert (data_format == "CCEE" or  data_format == "MONT"), "Unknown Data Format"
    if (data_format == "CCEE"):
        rawdata = read_CCEE_data(datafile)
    elif (data_format == "MONT"):
        rawdata = read_MONT_data(datafile)
    #
    tseries = prep_time_series(rawdata)
    #
    unique_vals, repeated_vals = repvals(tseries)
    #
    gaps = check_tinverval(unique_vals, interval=10)
    #
    new_metdataf = del_rep_values_metdata(rawdata, repeated_vals)
    #
    return gaps, new_metdataf
