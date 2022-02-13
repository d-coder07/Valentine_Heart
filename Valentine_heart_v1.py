###################################
############  Author:  ############
####### Devendra G Thombre ########
###################################
###################################
#########  Valentine_v1  ##########
###################################
###################################

# importing modules
import matplotlib.pyplot as plt
import numpy as np
import math
import time

# creating two x axis array for plotting in positive & negative x-axis:
x1 = np.arange(0,2.001,0.001)
x2 = np.arange(0,-2.001,-0.001)

# creating four y axis array for plotting in positive & negative y-axis in all four quadrant:
y1 = []
y2 = []
y3 = []
y4 = []

#straight line plotting arrays
x = np.arange(-2,3,0.1)
y = []
for i in (x):
    temp = 0.8*i-0.7
    y.append(temp)

#First quadrant y1 location
for i in (x1):
    t1 = 1 -((i-1)**2)
    temp = math.sqrt(t1)
    y1.append(temp)
    
#Second quadrant y2 location    
for i in (x2):
    t1 = 1 -((-i-1)**2)
    temp = math.sqrt(t1)
    y2.append(temp)

#Third quadrant y3 location       
for i in (x2):
    m = -2.5
    t1 = 1 - math.sqrt(-i/2)
    temp = math.sqrt(t1)
    temp *= m 
    y3.append(temp)

#Fourth quadrant y4 location   
for i in (x1):
    m = -2.5
    t1 = 1 - math.sqrt(i/2)
    temp = math.sqrt(t1)
    temp *= m 
    y4.append(temp)      
    
# adding style to plot
plt.style.use('ggplot')

# More style for plot:
#[‘Solarize_Light2’, ‘_classic_test_patch’, ‘bmh’, ‘classic’, ‘dark_background’, ‘fast’,
#‘fivethirtyeight’, ‘ggplot’,’grayscale’,’seaborn’,’seaborn-bright’,’seaborn-colorblind’, 
#‘seaborn-dark’, ‘seaborn-dark-palette’, ‘seaborn-darkgrid’, ‘seaborn-deep’, ‘seaborn-muted’,
#‘seaborn-notebook’, ‘seaborn-paper’, ‘seaborn-pastel’, ‘seaborn-poster’,’seaborn-talk’,
#’seaborn-ticks’,’seaborn-white’,’seaborn-whitegrid’,’tableau-colorblind10′]

# title of plot
plt.title("Happy Valentine Day!!")

# adding vertical y-axis line with -- line
plt.axvline(0, c='blue', ls='--')

# adding horizontal x-axis line with -- line
plt.axhline(0, c='blue', ls='--')

# label to x axis
plt.xlabel("X axis")

# label to y axis
plt.ylabel("Y axis")

# creating plot of heart
plt.plot(x1, y1, c="red")
plt.plot(x2, y2, c="red")
plt.plot(x2, y3, c="red")
plt.plot(x1, y4, c="red")

# creating straight line through heart
#plt.plot(x, y, c="red")

# plot show
plt.show()
