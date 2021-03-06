def repvals(tseries):
    ##
    '''Return repeated time values a time series.

       Argument: 
                tseries: a time series vector

       Output:
                pandas series with repeated elements as index and number of appearances as data.
 
       By UHU April 23, 2015'''
    ##
    import numpy as np
    import pandas as pd
    ##
    reps_els = [] ## Repeated elements vector
    times_rep = [] ## Times repeated
    ##
    uniques = tseries.unique()
    ##
    ncounts = tseries.value_counts()
    boolean = ncounts > 1
    ##
    ##
    for date_time in boolean.index:
        ##
        if (boolean[date_time]):
            print "Element at ", date_time, " repeated ", ncounts[date_time]
            reps_els.append(date_time)
            times_rep.append(ncounts[date_time])
        ##
    ##
    return uniques, pd.Series(index = reps_els, data = times_rep)

            
