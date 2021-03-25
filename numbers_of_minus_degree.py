from seperate_year import matrix_2015, matrix_2016, matrix_2017, matrix_2018, matrix_2019
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#definition for time value and temperature value for each year as list
time_value_2015 = []
temperature_value_2015 = []
time_value_2016 = []
temperature_value_2016 = []
time_value_2017 = []
temperature_value_2017 = []
time_value_2018 = []
temperature_value_2018 = []
time_value_2019 = []
temperature_value_2019 = []
time_value_2020 = []
temperature_value_2020 = []

for i in range(matrix_2015.shape[0]):
    if matrix_2015[i][1] < 0:
        time_value_2015.append(matrix_2015[i][0])
        temperature_value_2015.append(matrix_2015[i][1])
for i in range(matrix_2016.shape[0]):
    if matrix_2016[i][1] < 0:
        time_value_2016.append(matrix_2016[i][0])
        temperature_value_2016.append(matrix_2016[i][1])
for i in range(matrix_2017.shape[0]):
    if matrix_2017[i][1] < 0:
        time_value_2017.append(matrix_2017[i][0])
        temperature_value_2017.append(matrix_2017[i][1])
for i in range(matrix_2018.shape[0]):
    if matrix_2018[i][1] < 0:
        time_value_2018.append(matrix_2018[i][0])
        temperature_value_2018.append(matrix_2018[i][1])
for i in range(matrix_2019.shape[0]):
    if matrix_2019[i][1] < 0:
        time_value_2019.append(matrix_2019[i][0])
        temperature_value_2019.append(matrix_2019[i][1])

points_in_year = [len(time_value_2015), len(time_value_2016), len(time_value_2017), len(time_value_2018), len(time_value_2019)]
year = ['2015', '2016', '2017', '2018', '2019']
print(points_in_year)


fig,minus = plt.subplots()
minus.set_xlabel('year')
minus.set_ylabel('numbers of minus degree')
minus.set_title('numbers of minus degree')

for i in range(5):
    plt.bar(year[i], points_in_year[i])

plt.savefig('numbers of minus degree')


plt.show()