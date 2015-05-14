def quality_control(datafile, tmin, tmax, data_format = "CCEE", frequency = 10, tzone = "none", dst = True, iprint = 0):
    ''' Docstring...Fernando'''
    ##
    import numpy as np
    import pandas as pd
    ##
    from defined_functions import read_CCEE_data, read_MONT_data, prep_time_series, repvals, check_tinterval, del_rep_values_metdata, prepare_full_exp_tseries, trim_dates
    #
    print data_format
    assert (data_format == "CCEE" or  data_format == "MONT"), "Unknown Data Format"
    if (data_format == "CCEE"):
        rawdata = read_CCEE_data(datafile)
    elif (data_format == "MONT"):
        rawdata = read_MONT_data(datafile)
    #
    tseries = prep_time_series(rawdata, timezone = tzone, dst = dst)
    #
    unique_vals, repeated_vals = repvals(tseries)
    #
    gaps = check_tinterval(unique_vals, interval=10, iprint = iprint)
    #
    gaps = trim_dates(tmin, tmax, gaps)
    #
    new_metdataf = del_rep_values_metdata(rawdata, repeated_vals)
    #
    new_metdataf = prepare_full_exp_tseries(tmin, tmax, new_metdataf, frequency = frequency, timezone = tzone)
    #
    return gaps, new_metdataf
