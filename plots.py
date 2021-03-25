import find_max_and_min
import matplotlib.pyplot as plt

#import the data for hottest and coldest time+value from other package
hottest_time, coldest_time = find_max_and_min.find_max_min()

#define the list of time and value for hottest and coldest time
#purpose of the list time_hot and time_cold is to store the string data from ndarray hottest_time and coldest_time
#using string to seperate time of day from large number with original form of yyyymmddhhmmss
time_hot = []
value_hot = []
time_cold = []
value_cold = []
for i in range(hottest_time.shape[0]):
    time_hot.append(str(hottest_time[i][0])) #extract numbers from hottest_time and change it to string
    value_hot.append(hottest_time[i][1]) #the size of the list for value match the size of the list for time
for i in range(coldest_time.shape[0]):
    time_cold.append(str(coldest_time[i][0])) #extract numbers from coldest_time and change it to string
    value_cold.append(coldest_time[i][1]) #the size of the list for value match the size of the list for time

#the following list store string information of time and year
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

#create a new figure
plt.figure(1,dpi=600,figsize=(30,30))
fig,hot=plt.subplots() #define the subplot hot
hot.plot(time_hot,value_hot,color='red') #use data from time_hot and value_hot to plot
hot.scatter(time_hot,value_hot,color='green') #drow scatter and set color
hot.set_xlabel('time in day') #set xlabel
hot.set_ylabel('temperatrue') #set ylabel
hot.set_title('hottest time') #set title
plt.xticks(plt.xticks()[0],time_of_day_hot) #set each ticks on x axis

#add year-information on the scatter with plt.annotate
for i in range(len(time_hot)):
    plt.annotate(year_hot[i],(time_hot[i],value_hot[i]))

plt.savefig('hottest time') #save the figure

#create new figure for coldest time
plt.figure(2,dpi=600,figsize=(30,30))
fig,cold=plt.subplots() #define subplot for coldest time
cold.plot(time_cold,value_cold,color='blue') #use data from time_cold and value_cold to plot
cold.scatter(time_cold,value_cold,color='yellow') #drow scatter and set color
cold.set_xlabel('time in day') #set xlabel
cold.set_ylabel('temperatrue') #set ylabe
cold.set_title('coldest time ') #set title
plt.xticks(plt.xticks()[0],time_of_day_cold) #set ticks for x axis

#add year-information on the scatter with plt.annotate
for i in range(len(time_cold)):
    plt.annotate(year_cold[i],(time_cold[i],value_cold[i]))

plt.savefig('coldest time') #save the figure
plt.show() #show figures on screen



