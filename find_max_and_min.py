import pandas as pd
import numpy as np
import seperate_year

#import data from other package
matrix_2015, matrix_2016, matrix_2017, matrix_2018, matrix_2019, matrix_2020, time_value_2015,\
temperature_value_2015, time_value_2016, temperature_value_2016, time_value_2017, temperature_value_2017,\
time_value_2018, temperature_value_2018, time_value_2019, temperature_value_2019, time_value_2020,\
temperature_value_2020 = seperate_year.data_in_year()

#find the maximum with np.amax(), use np.where() to get the index of rows,
#we can have the information of time and temperature with the index of rows
hottest_2015 = matrix_2015[np.where(matrix_2015[:,1] == np.amax(matrix_2015[:,1]))]
hottest_2016 = matrix_2016[np.where(matrix_2016[:,1] == np.amax(matrix_2016[:,1]))]
hottest_2017 = matrix_2017[np.where(matrix_2017[:,1] == np.amax(matrix_2017[:,1]))]
hottest_2018 = matrix_2018[np.where(matrix_2018[:,1] == np.amax(matrix_2018[:,1]))]
hottest_2019 = matrix_2019[np.where(matrix_2019[:,1] == np.amax(matrix_2019[:,1]))]
hottest_2020 = matrix_2020[np.where(matrix_2020[:,1] == np.amax(matrix_2020[:,1]))]

#put all hottest time together
hottest_time = np.row_stack((hottest_2015,hottest_2016,hottest_2017,hottest_2018,hottest_2019,hottest_2020))
df_hot = pd.DataFrame(hottest_time,columns=['time','temperature']) #change the array to pandas data frame
df_hot.to_csv('hottest_time.csv') #out put as csv file

#find the minimum with np.amin(), use np.where() to get the index of rows
coldest_2015 = matrix_2015[np.where(matrix_2015[:,1] == np.amin(matrix_2015[:,1]))]
coldest_2016 = matrix_2016[np.where(matrix_2016[:,1] == np.amin(matrix_2016[:,1]))]
coldest_2017 = matrix_2017[np.where(matrix_2017[:,1] == np.amin(matrix_2017[:,1]))]
coldest_2018 = matrix_2018[np.where(matrix_2018[:,1] == np.amin(matrix_2018[:,1]))]
coldest_2019 = matrix_2019[np.where(matrix_2019[:,1] == np.amin(matrix_2019[:,1]))]
coldest_2020 = matrix_2020[np.where(matrix_2020[:,1] == np.amin(matrix_2020[:,1]))]

#put all coldest time together
coldest_time = np.row_stack((coldest_2015,coldest_2016,coldest_2017,coldest_2018,coldest_2019,coldest_2020))
df_cold = pd.DataFrame(coldest_time,columns=['time','temperature']) #change the array to pandas data frame
df_cold.to_csv('coldest_time.csv') #out put as csv file

#function for further use
def find_max_min():
    return hottest_time, coldest_time
