def del_rep_values_metdata(rawdata, repvalues, col_label = "tdate"):
    ''' Given a data frame with a column labeled with name col_label and some repeated values repvalues returns a pandas data frame removing the repeated time instances.

        Argument: 
                rawdata   : pandas data frame with data
                repvalues : repeated values (output of repeated_values_vec)
                col_label : column label of repeated dates (optional, default value = "tdate")

        Output: 
                rawdata removing repeated instances in tdate column.

        By UHU April 23, 2015'''
    import numpy as np
    import pandas as pd
    #
    delind = [] ## rawdat index values to be deleted
    #
    for rep_index in repvalues.index:
        for delete_index in rawdata[rawdata[col_label]==rep_index].index[1:]:
            delind.append(delete_index)
    #
    return rawdata.drop(delind)
