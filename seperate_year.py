import new_time_step
import numpy as np
import pandas as pd

#import data from python file new_time_step
file,matrix,matrix_new,df=new_time_step.read_csv_file()



#definition for time value and temperature value for each year as list
time_value_2015=[]
temperature_value_2015=[]
time_value_2016=[]
temperature_value_2016=[]
time_value_2017=[]
temperature_value_2017=[]
time_value_2018=[]
temperature_value_2018=[]
time_value_2019=[]
temperature_value_2019=[]
time_value_2020=[]
temperature_value_2020=[]

#select time and temperature values for different years and store them in lists
for i in range(matrix_new.shape[0]):
    if matrix_new[i][2]<201600000000:
        time_value_2015.append(matrix_new[i][2])
        temperature_value_2015.append(matrix_new[i][3])
    if 201600000000<matrix_new[i][2]<201700000000:
        time_value_2016.append(matrix_new[i][2])
        temperature_value_2016.append(matrix_new[i][3])
    if 201700000000<matrix_new[i][2]<201800000000:
        time_value_2017.append(matrix_new[i][2])
        temperature_value_2017.append(matrix_new[i][3])
    if 201800000000<matrix_new[i][2]<201900000000:
        time_value_2018.append(matrix_new[i][2])
        temperature_value_2018.append(matrix_new[i][3])
    if 201900000000<matrix_new[i][2]<202000000000:
        time_value_2019.append(matrix_new[i][2])
        temperature_value_2019.append(matrix_new[i][3])
    if 202000000000<matrix_new[i][2]<202100000000:
        time_value_2020.append(matrix_new[i][2])
        temperature_value_2020.append(matrix_new[i][3])

#comebine time and temperature values in numpy array
matrix_2015 = np.column_stack((time_value_2015, temperature_value_2015))
matrix_2016 = np.column_stack((time_value_2016, temperature_value_2016))
matrix_2017 = np.column_stack((time_value_2017, temperature_value_2017))
matrix_2018 = np.column_stack((time_value_2018, temperature_value_2018))
matrix_2019 = np.column_stack((time_value_2019, temperature_value_2019))
matrix_2020 = np.column_stack((time_value_2020, temperature_value_2020))

#change numpy array to pandas dataframe
df_2015=pd.DataFrame(matrix_2015,columns=list(['Zeitstempel','Wert']))
df_2016=pd.DataFrame(matrix_2016,columns=list(['Zeitstempel','Wert']))
df_2017=pd.DataFrame(matrix_2017,columns=list(['Zeitstempel','Wert']))
df_2018=pd.DataFrame(matrix_2018,columns=list(['Zeitstempel','Wert']))
df_2019=pd.DataFrame(matrix_2019,columns=list(['Zeitstempel','Wert']))
df_2020=pd.DataFrame(matrix_2020,columns=list(['Zeitstempel','Wert']))

#output the dataframe as csv file
df_2015.to_csv('data_2015.csv')
df_2016.to_csv('data_2016.csv')
df_2017.to_csv('data_2017.csv')
df_2018.to_csv('data_2018.csv')
df_2019.to_csv('data_2019.csv')
df_2020.to_csv('data_2020.csv')

#function for further use
def data_in_year():
    return matrix_2015, matrix_2016, matrix_2017, matrix_2018, matrix_2019, matrix_2020, time_value_2015,\
           temperature_value_2015, time_value_2016, temperature_value_2016, time_value_2017, temperature_value_2017,\
           time_value_2018, temperature_value_2018, time_value_2019, temperature_value_2019, time_value_2020,\
           temperature_value_2020



