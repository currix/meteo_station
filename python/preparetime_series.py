def prep_time_series(data_frame_name):
    '''Given a data frame with meteorological data having a column labeld "time" and a column labeled "date" returns the same data frame adding a new column labeled "tdate" with a time series of combined data of dates and time columns.

       Argument: 
                data_frame_name  : meteorology data frame

       Output:
               pandas data frame with a "tdate" column which has time data for each event.
                
       By UHU April 23, 2015'''
    import numpy as np
    import pandas as pd
    from dateutil.parser import parse
    ##
    ##
    data_date = data_frame_name.date
    data_time = data_frame_name.time
    ##
    timedata = [];
    ##
    for ind in data_frame_name.index:
        timedata.append( parse(data_date[ind]+' '+data_time[ind], dayfirst=True) )
    ##
    ##  Add new column with timedates
    data_frame_name["tdate"] = pd.Series(timedata, index=data_frame_name.index)
    ##
    return pd.Series(timedata)
        
