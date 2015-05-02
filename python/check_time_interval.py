def check_tinverval(tseries, interval=10):
    ##
    '''Return elements in the time series tseries that don't have the given frequency interval. The argument interval is given in units of minutes with a default value of 10 minutes.

       Arguments: 
                  tseries :  time series
                  interval:  time interval in minutes (default val = 10 min)

       Output:
                  pandas series with data = irregular periods and index = times when irregular periods happen.

       By UHU April 23, 2015'''
    ##
    import numpy as np
    import pandas as pd
    ##
    date_time_0 = tseries[0]
    irr_times = []
    irr_period = []
    ##
    for date_time in tseries[1:]:
        ##
        delta = date_time - date_time_0
        ##
        if (delta.seconds/60 != interval or delta.days != 0 ): ## Transforms seconds to mins
            ##
            print "Irregular measure: ", date_time_0, date_time, delta
            irr_times.append(date_time_0)
            irr_period.append(delta.seconds/60+delta.days*24*60)
        ##
        date_time_0 = date_time
    ##
    return pd.Series(data = irr_period, index = irr_times)
            
