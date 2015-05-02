def create_full_tseries(initial_date, final_date):
    ##
    '''Given an initial and a final dates, build pandas time series between in the given interval with periodicities of 10 minutes, 1 hour, 1 day and 1 month.

    Arguments:

    Output:


       By UHU April 23, 2015'''
    ##
    import pandas
    #
    full_time_series_10min = pandas.date_range(initial_date,final_date,freq="10min")
    #
    full_time_series_hourly = pandas.date_range(initial_date, final_date,freq="1H")
    #
    full_time_series_daily = pandas.date_range(initial_date, final_date,freq="1D")
    #
    full_time_series_monthly = pandas.date_range(initial_date, final_date,freq="1M")
    return full_time_series_10min, full_time_series_hourly, full_time_series_daily, full_time_series_monthly  
    





        

    
