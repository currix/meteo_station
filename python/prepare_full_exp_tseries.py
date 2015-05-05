def prepare_full_exp_tseries(t_min, t_max, metdata, frequency = 10):
    '''Fernando...'''
    import numpy as np
    import pandas as pd
    from datetime import datetime
    from datetime import timedelta
    from dateutil.parser import parse
    ##
    t_ini = parse(t_min, dayfirst=True)
    t_end = parse(t_max, dayfirst=True)
    #
    # Chop series
    #
    deleted_indexes = []
    for ivalue in metdata.index:
        #
        time_value = metdata.tdate[ivalue]
        #
        if (time_value < t_ini or time_value > t_end):
            deleted_indexes.append(ivalue)
    #
    chopped_dframe = metdata.drop(deleted_indexes)
    chopped_dframe_date = chopped_dframe.set_index("tdate")
    #
    full_time_series_10min = pd.date_range(t_ini,t_end,freq="10min")
    #
    return chopped_dframe_date.reindex(full_time_series_10min)
