import find_max_and_min_15mins
import matplotlib.pyplot as plt

# import the data for hottest and coldest time+value from other package
hottest_time, coldest_time = find_max_and_min_15mins.find_max_min()

# define the list of time and value for hottest and coldest time
# purpose of the list time_hot and time_cold is to store the string data from ndarray hottest_time and coldest_time
# using string to separate time of day from large number with original form of yyyymmddhhmmss
time_hot = []
value_hot = []
time_cold = []
value_cold = []
for i in range(hottest_time.shape[0]):
    time_hot.append(str(hottest_time[i][0]))  # extract numbers from hottest_time and change it to string
    value_hot.append(hottest_time[i][1])  # the size of the list for value match the size of the list for time
for i in range(coldest_time.shape[0]):
    time_cold.append(str(coldest_time[i][0]))  # extract numbers from coldest_time and change it to string
    value_cold.append(coldest_time[i][1])  # the size of the list for value match the size of the list for time

# the following list store string information of time and year
time_of_day_hot = []
time_of_day_cold = []
year_hot = []
year_cold = []

for i in range(len(time_hot)):
    time_of_day_hot.append(time_hot[i][8:10]+':'+time_hot[i][10:12])
    year_hot.append(time_hot[i][0:4])
for i in range(len(time_cold)):
    time_of_day_cold.append(time_cold[i][8:10]+':'+time_cold[i][10:12])
    year_cold.append(time_cold[i][0:4])

# create a new figure
fig, hot = plt.subplots()
hot.plot(time_hot, value_hot, color='red')  # use data from time_hot and value_hot to plot
hot.scatter(time_hot, value_hot, color='green')  # draw scatter and set color
hot.set_xlabel('time in day')  # set label on x axis
hot.set_ylabel('temperature')  # set label on y axis
hot.set_title('hottest time')  # set title
plt.xticks(plt.xticks()[0], time_of_day_hot)  # set each ticks on x axis

# add year-information on the scatter with plt.annotate
for i in range(len(time_hot)):
    plt.annotate(year_hot[i], (time_hot[i],value_hot[i]))

plt.savefig(r'analysis based on 15mins intervals\hottest time 15mins', dpi=300)  # save the figure

# create new figure for coldest time
fig, cold = plt.subplots()
cold.plot(time_cold, value_cold, color='blue')  # use data from time_cold and value_cold to plot
cold.scatter(time_cold, value_cold, color='yellow')  # draw scatter and set color
cold.set_xlabel('time in day')  # set label on x axis
cold.set_ylabel('temperature')  # set label on y axis
cold.set_title('coldest time ')  # set title
plt.xticks(plt.xticks()[0], time_of_day_cold)  # set ticks for x axis

# add year-information on the scatter with plt.annotate
for i in range(len(time_cold)):
    plt.annotate(year_cold[i], (time_cold[i], value_cold[i]))

plt.savefig(r'analysis based on 15mins intervals\coldest time 15mins', dpi=300)  # save the figure
plt.show()  # show figures on screen




