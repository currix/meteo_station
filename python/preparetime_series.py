def prep_time_series(data_frame_name):
    '''To be written by Fernando'''
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
        
