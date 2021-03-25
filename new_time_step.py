import pandas as pd
import numpy as np

file = pd.read_csv('temperatures.csv') #Read the file 'temperatures.csv' by using pandas
matrix = file.to_numpy() #change dataframe to numpy array, because numpy works faster

#create a new np array for new structure with 15-minutes-intervals
matrix_new = np.zeros((4*matrix.shape[0], matrix.shape[1]), dtype=object)



#set values for columns 'Produkt_Code','SDO_ID','Qualitaet_Niveau','Qualitaet_Byte', they are the same as the input values
for i in range(matrix.shape[0]):
    matrix_new[i * 4][0] = matrix[i][0]
    matrix_new[i * 4 + 1][0] = matrix[i][0]
    matrix_new[i * 4 + 2][0] = matrix[i][0]
    matrix_new[i * 4 + 3][0] = matrix[i][0]

    matrix_new[i * 4][1] = matrix[i][1]
    matrix_new[i * 4 + 1][1] = matrix[i][1]
    matrix_new[i * 4 + 2][1] = matrix[i][1]
    matrix_new[i * 4 + 3][1] = matrix[i][1]

    matrix_new[i * 4][4] = matrix[i][4]
    matrix_new[i * 4 + 1][4] = matrix[i][4]
    matrix_new[i * 4 + 2][4] = matrix[i][4]
    matrix_new[i * 4 + 3][4] = matrix[i][4]

    matrix_new[i * 4][5] = matrix[i][5]
    matrix_new[i * 4 + 1][5] = matrix[i][5]
    matrix_new[i * 4 + 2][5] = matrix[i][5]
    matrix_new[i * 4 + 3][5] = matrix[i][5]

    #now set values for the column 'Zeitstempel'
    matrix_new[i * 4][2] = matrix[i][2]
    matrix_new[i * 4 + 1][2] = matrix_new[i * 4][2]+15
    matrix_new[i * 4 + 2][2] = matrix_new[i * 4 + 1][2] + 15
    matrix_new[i * 4 + 3][2] = matrix_new[i * 4 + 2][2] + 15

#now set values for the column 'Wert'
#linear interpolation: Y[k]=Y[i]+(Y[i+1]-Y[i])*(X[k]-X[i])/(X[i+1]-X[i])
#we set X[i]=0,X[i+1]=60,X[k]=15,30,45
for i in range(matrix.shape[0]-1):  #the last 3 values are not included here
    matrix_new[i * 4][3] = matrix[i][3]
    matrix_new[i * 4 + 1][3] = matrix[i][3]+(15/60)*(matrix[i+1][3]-matrix[i][3])
    matrix_new[i * 4 + 2][3] = matrix[i][3]+(30/60)*(matrix[i+1][3]-matrix[i][3])
    matrix_new[i * 4 + 3][3] = matrix[i][3]+(45/60)*(matrix[i+1][3]-matrix[i][3])

#now set the last 3 values for the column 'Wert'
#assum the max.value of matrix.shape[0]=a,Y[k]=(Y[a-1]-Y[a-2])*(X[k]/60)+Y[a-2],X[k]=75,90,105
matrix_new[4*(matrix.shape[0]-1)][3] = matrix[matrix.shape[0]-1][3]
matrix_new[4*(matrix.shape[0]-1)+1][3] = (matrix[matrix.shape[0]-1][3]-matrix[matrix.shape[0]-2][3])*(75/60)\
                                         + matrix[matrix.shape[0]-2][3]
matrix_new[4*(matrix.shape[0]-1)+2][3] = (matrix[matrix.shape[0]-1][3]-matrix[matrix.shape[0]-2][3])*(90/60)\
                                         + matrix[matrix.shape[0]-2][3]
matrix_new[4*(matrix.shape[0]-1)+3][3] = (matrix[matrix.shape[0]-1][3]-matrix[matrix.shape[0]-2][3])*(105/60)\
                                         + matrix[matrix.shape[0]-2][3]

#change the numpy array into a new dataframe
df = pd.DataFrame(matrix_new, columns=list(['Produkt_Code', 'SDO_ID', 'Zeitstempel',
                                                                'Wert', 'Qualitaet_Niveau', 'Qualitaet_Byte']))

#output the data into .csv file
df.to_csv('result_15_minutes_intervals.csv')


#function for further usage
def read_csv_file ():
    return file,matrix,matrix_new,df
