def prepare_full_exp_tseries(t_min, t_max, metdata, frequency = 10, timezone = "none"):
    '''Fernando...'''
    import numpy as np
    import pandas as pd
    from datetime import datetime
    from datetime import timedelta
    from dateutil.parser import parse
    import pytz
    ##
    #
    # Fernando: Include assert checking t_ini < t_end
    # 
    t_ini = parse(t_min, dayfirst=True)
    t_end = parse(t_max, dayfirst=True)
    # Offset-aware time
    if (timezone != "none"):
        utc = pytz.timezone('UTC')
        t_ini = utc.normalize(utc.localize(t_ini))
        t_end = utc.normalize(utc.localize(t_end))
    #
    # Chop series
    #
    deleted_indexes = []
    ##
    if (timezone != "none"):
        #
        boolmat = np.logical_or(metdata.tdate_utc >= t_ini, metdata.tdate_utc <= t_end)
        #
    else:
        #        
        boolmat = np.logical_or(metdata.tdate >= t_ini, metdata.tdate <= t_end)
        #
    # Removing dataframe entries with a boolean vector
    chopped_dframe = metdata.drop(boolmat)
    #
    # Set data as index
    if (timezone != "none"):
        chopped_dframe_date = chopped_dframe.set_index("tdate_utc")
    else:
        chopped_dframe_date = chopped_dframe.set_index("tdate")
    #
    # Build full time series
    if (timezone != "none"):    
        full_time_series_10min = pd.date_range(t_ini,t_end,freq="10min", tz="UTC")
    else:
        full_time_series_10min = pd.date_range(t_ini,t_end,freq="10min")
    #
    return chopped_dframe_date.reindex(full_time_series_10min)
