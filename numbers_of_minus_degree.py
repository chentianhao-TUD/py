from separate_year_15min_intervals import matrix_2015, matrix_2016, matrix_2017, matrix_2018, matrix_2019
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# in this program i am trying to find out how many measurements of the temperature are below 0 degree for each year
# definition for time value and temperature value for each year as list
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

# find temperature that below 0 degree and store them in lists for each year

for i in range(matrix_2015.shape[0]):
    if matrix_2015[i][1] < 0:                             # select temperature below 0 degree
        time_value_2015.append(matrix_2015[i][0])         # time information for minus degree, same for other years
        temperature_value_2015.append(matrix_2015[i][1])  # temperature value that below 0 degree, same for other years

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

# count numbers of minus degree
numbers_in_year = [len(time_value_2015), len(time_value_2016), len(time_value_2017), len(time_value_2018),
                   len(time_value_2019)]
labels_year = ['2015', '2016', '2017', '2018', '2019']  # labels on x axis
color = ['red', 'blue', 'orange', 'green', 'pink']  # color for the bars
x = np.arange(len(labels_year))  # location for x labels
width = 0.5  # width of each bar

# create a figure
fig, minus = plt.subplots()
rect = minus.bar(x, numbers_in_year, width, color=color)  # draw bars with the data
minus.set_xlabel('year')                     # set label on y axis
minus.set_ylabel('numbers of minus degree')  # set label on y axis
minus.set_title('numbers of minus degree')   # set title
minus.set_xticks(x)                          # set ticks position on x axis
minus.set_xticklabels(labels_year)           # set ticks label on x axis

# show the numbers on top of each bar
for i in range(len(labels_year)):
    plt.text(x[i]-0.15, numbers_in_year[i]+10, str(numbers_in_year[i]))

plt.savefig('numbers of minus degree', dpi=300)  # save image
plt.show()  # show on the screen

