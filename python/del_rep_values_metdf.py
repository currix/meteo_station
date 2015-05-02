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
