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
