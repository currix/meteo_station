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
