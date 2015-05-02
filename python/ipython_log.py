# IPython log file

get_ipython().magic(u'pinfo %logstart')
get_ipython().magic(u'logstart')
import pandas
import numpy as np
testdata = pandas.read_table("test_meteofisica.dat",header=None, names=['abstime','date','time','Tin','Tout','Tmax','Tmin','x1','x2','x3','Solar Rad','Solar Rad Hi','UVRad','UVRad Hi','UV dose','Pressure','Wind Speed','Wind Speed Hi','Wind Direction','Wind Chill','Rain','Rain Max','H in','H out','Dew point'], sep='\s+')
testdata = pandas.read_table("../data/test_meteofisica.dat",header=None, names=['abstime','date','time','Tin','Tout','Tmax','Tmin','x1','x2','x3','Solar Rad','Solar Rad Hi','UVRad','UVRad Hi','UV dose','Pressure','Wind Speed','Wind Speed Hi','Wind Direction','Wind Chill','Rain','Rain Max','H in','H out','Dew point'], sep='\s+')
get_ipython().magic(u'pinfo pandas.save')
pandas.save(testdata, "test_saving_dataframe")
aaa = pandas.load("test_saving_dataframe")
aaa == testdata
aaa.type
aaa[abstime]
aaa["abstime"]
testdata["abstime"]
testdata["abstime"]==aaa["abstime"]
get_ipython().magic(u'run read_CCEE_station_data.py')
get_ipython().magic(u'run read_CCEE_station_data.py')
read_CCEE_data("../data/test_meteofisica.dat")
testdata = read_CCEE_data("../data/test_meteofisica.dat")
testdata["abstime"]==aaa["abstime"]
data = read_CCEE_data("../data/meteofisica.dat")
data = read_CCEE_data("../data/meteofisica_data.dat")
abstimes = testdata["abstime"]
abstimes.type
abstimes.type()
abstimes.shape
abstimes
abstimes = np.array[testdata["abstime"]]
abstimes = np.array(testdata["abstime"])
abstimes.shape
abstimes
abostimes.shape[1]
abstimes.shape[1]
abstimes.shape()
abstimes.shape
abstimes.shape-1
abstimes.shape[0]
np.zeros(10)
a = 1
a++
get_ipython().magic(u'run forward_difference.py')
fwd_diff(np.array([1,2,4,6,98,100]))
fwd_diff(abstimes)
abstimes = np.array(data["abstime"])
fwd_diff(abstimes)
import pyplot from matplotlib
use pyplot from matplotlib
from matplotlib import pyplot
pyplot.plot(abstimes)
pyplot.show()
abstimes_diff = fwd_diff(abstimes)
pyplot.plot(abstimes_diff)
pyplot.show()
pyplot.plot(abstimes)
pyplot.show()
pyplot.plot(abstimes_diff)
pyplot.show()
pyplot.plot(abstimes_diff)
pyplot.ylim(-1,1000)
pyplot.show()
pyplot.plot(abstimes_diff)
pyplot.ylim(-1,1300)
pyplot.show()
exit()
