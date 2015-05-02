def create_full_tseries(initial_date, final_date):
    '''Use to categorize in gropus of 10 minutes, hours, days and months a column with dates and times.
       By UHU April 23, 2015'''
    #
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
    





        

    
