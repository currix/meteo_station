def check_tinterval(tseries, interval=10, iprint = 0):
    ##
    '''Return elements in the time series tseries that don't have the given frequency interval. The argument interval is given in units of minutes with a default value of 10 minutes.

       Arguments :
             tseries  :  time series
             interval :  time interval in minutes (optional, default val = 10 min)
             iprint   :  verbosity control. (optional, default value = 0, min output)

       Output:
                  pandas series with data = irregular periods and index = times when irregular periods happen.

       By UHU April 23, 2015'''
    ##
    import numpy as np
    import pandas as pd
    from datetime import datetime
    from datetime import timedelta  
    ##
    date_time_0 = tseries[0]
    irr_times = []
    irr_period = []
    ##
    for date_time in tseries[1:]:
        ##
        delta = date_time - date_time_0
        ##
        if (iprint > 0):
            print date_time, date_time_0, delta
        ##
###        if (delta/np.timedelta64(1, 'm') != interval ): ## numpy timedelta
        if (delta.seconds/60 != interval or delta.days != 0 ): ## Transforms seconds to mins
            ##
            if (iprint > 0):
                print "Irregular measure: ", date_time_0, date_time, delta
###             print "Irregular measure: ", date_time_0, date_time, delta/np.timedelta64(1, 'm')
            irr_times.append(date_time_0)
#
            irr_period.append(delta.seconds/60+delta.days*24*60)
###            irr_period.append( delta/np.timedelta64(1, 'm') )
        ##
        date_time_0 = date_time
    ##
    return pd.Series(data = irr_period, index = irr_times)
            
