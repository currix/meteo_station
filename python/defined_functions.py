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
        
def read_CCEE_data(filename, rawdata = True):
    ###
    '''Read data using the CCEE station format.
       Argument: data filename.
       By Curro March 18, 2015'''
    ###
    import numpy as np
    import pandas
    #
    if (rawdata):
        return pandas.read_table(filename,header=None, names=['date','time','Tin','Tout','Tmax','Tmin','x1','x2','x3','Solar Rad','Solar Rad Hi','UVRad','UVRad Hi','UV dose','Pressure','Wind Speed','Wind Speed Hi','Wind Direction','Wind Chill','Rain','Rain Max','H in','H out','Dew point'], sep='\s+')
    else:
        return pandas.read_table(filename,header=None, names=['abstime','date','time','Tin','Tout','Tmax','Tmin','x1','x2','x3','Solar Rad','Solar Rad Hi','UVRad','UVRad Hi','UV dose','Pressure','Wind Speed','Wind Speed Hi','Wind Direction','Wind Chill','Rain','Rain Max','H in','H out','Dew point'], sep='\s+')
def read_MONT_data(filename):
    ###
    '''Read data using the MONT station format.
       Argument: data filename.
       By Fernando & Curro April 15, 2015'''
    ###
    import numpy as np
    import pandas
    #
    return pandas.read_table(filename,header=None,skiprows=2,names=['date','time','Tout','Tmax','Tmin','H out','Dew point','Wind Speed','Wind Direction','Wind Rec','Wind Speed Hi','Wind Direction Hi','Wind Chill','Heat Index','THM Index','Pressure','Rain','Rain Max','GDC','GDF','Tin','H in','Dew Point In','Heat Index In','M Wind','Tx Wind','ISS Rec','Arc INT'], sep='\s+')
def repvals(tseries):
    ##
    '''Fernando lo va a escribir esto...'''
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

            
def check_tinverval(tseries, interval=10):
    ##
    '''Fernando lo va a escribir esto...'''
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
            
def del_rep_values_metdata(rawdata, repvalues):
    ''' Delete repeated time values from data file... Fernando will complete this...'''
    import numpy as np
    import pandas as pd
    #
    delind = [] ## rawdat index values to be deleted
    #
    for rep_index in repvalues.index:
        for delete_index in rawdata[rawdata["tdate"]==rep_index].index[1:]:
            delind.append(delete_index)
    #
    return rawdata.drop(delind)
