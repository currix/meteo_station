def prep_time_series(data_frame_name, timezone = "none", dst = True):
    '''Given a data frame with meteorological data having a column labeld "time" and a column labeled "date" returns the same data frame adding a new column labeled "tdate" with a time series of combined data of dates and time columns.

       Argument: 
                data_frame_name  : meteorology data frame
                timezone         : (optional, default value none) data time zone e.g. "CET" or "UTC"
                dst              : (optional, default value True) use daylight saving time

       Output:
               pandas data frame with a "tdate" column which has time data for each event and a "tdate_utc" column with offset aware time. If timezone information is given the output is expressed in UTC.
                
       By UHU April 13, 2015'''
    import numpy as np
    import pandas as pd
    from dateutil.parser import parse
    import pytz
    ##
    ##
    data_date = data_frame_name.date
    data_time = data_frame_name.time
    ##
    timedata = [];
    ##
    for ind in data_frame_name.index:
        timedata.append( parse(data_date[ind]+' '+data_time[ind], dayfirst=True) )
    ## tz stuff (offset aware time)
    if (timezone != "none"):
        # Add time zone info
        tzone = pytz.timezone(timezone)
        timedata_tz = map(lambda x: tzone.normalize(tzone.localize(x, is_dst=dst)), timedata) ## Add timezone info
        # Transform to UTC if the timezone is a local one
        if (timezone != "UTC"):
            utc = pytz.timezone('UTC')
            timedata_tz = map(lambda x: x.astimezone(utc), timedata_tz) ## Transform to UTC timezone 
    ##
    ##  Add new column with timedates
    data_frame_name["tdate"] = pd.Series(timedata, index=data_frame_name.index)
    if (timezone != "none"):
        data_frame_name["tdate_utc"] = pd.Series(timedata_tz, index=data_frame_name.index)
    ##
    return pd.Series(timedata)
        
