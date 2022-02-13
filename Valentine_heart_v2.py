#!/usr/bin/env python
###################################
############  Author:  ############
####### Devendra G Thombre ########
###################################
###################################
######  Valentine_heart_v2  #######
###################################
###################################

# importing modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math
import time

# adding style to plot
plt.style.use('dark_background')
# More style for plot:
#[‘Solarize_Light2’, ‘_classic_test_patch’, ‘bmh’, ‘classic’, ‘dark_background’, ‘fast’,
#‘fivethirtyeight’, ‘ggplot’,’grayscale’,’seaborn’,’seaborn-bright’,’seaborn-colorblind’, 
#‘seaborn-dark’, ‘seaborn-dark-palette’, ‘seaborn-darkgrid’, ‘seaborn-deep’, ‘seaborn-muted’,
#‘seaborn-notebook’, ‘seaborn-paper’, ‘seaborn-pastel’, ‘seaborn-poster’,’seaborn-talk’,
#’seaborn-ticks’,’seaborn-white’,’seaborn-whitegrid’,’tableau-colorblind10′]

fig1, ax1 = plt.subplots()

m1 =[]
m2 =[]
m3 =[]
m4 =[]
m5 =[]
m6 =[]
m7 =[]
m8 =[]
# creating two x axis array for plotting in positive & negative x-axis:
x1 = np.arange(0,2.01,0.01)
x2 = np.arange(0,-2.01,-0.01)

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
count_x1 = len(x1)
count_x2 = len(x2)
count_y1 = len(y1)
count_y2 = len(y2)
count_y3 = len(y3)
count_y4 = len(y4)
    



# creating plot of heart
#plt.plot(x1, y1, c="red")
#plt.plot(x2, y2, c="red")
#plt.plot(x2, y3, c="red")
#plt.plot(x1, y4, c="red")

def animate1(i):
    t1 = x1[i]
    t2= y1[i]
    m1.append(t1)
    m2.append(t2)
    ax1.plot(m1, m2, c= "red")


def animate2(i):
    t1 = x1[count_x1-i-1]
    t2= y4[count_y4-i-1]
    m3.append(t1)
    m4.append(t2)
    ax1.plot(m3, m4, c= "red")

        
def animate3(i):
    t1 = x2[i]
    t2= y3[i]
    m5.append(t1)
    m6.append(t2)
    ax1.plot(m5, m6, c= "red")


def animate4(i):
    t1 = x2[count_x2-i-1]
    t2= y2[count_y2-i-1]
    m7.append(t1)
    m8.append(t2)
    ax1.plot(m7, m8, c= "red")
    
## Plotting for graph animated
ani1 = FuncAnimation(fig1, animate1, frames=len(x1), interval=3, repeat=False)
ani2 = FuncAnimation(fig1, animate2, frames=len(x1), interval=3, repeat=False)
ani3 = FuncAnimation(fig1, animate3, frames=len(x2), interval=3, repeat=False)
ani4 = FuncAnimation(fig1, animate4, frames=len(x2), interval=3, repeat=False)


# creating straight line through heart
#plt.plot(x, y, c="red")

# title of plot
plt.title("Happy Valentine Day!!!")

# adding vertical y-axis line with -- line
##plt.axvline(0, c='blue', ls='--')

# adding horizontal x-axis line with -- line
##plt.axhline(0, c='blue', ls='--')

# label to x axis
plt.xlabel("X axis")

# label to y axis
plt.ylabel("Y axis")

# adding style to plot
plt.style.use('dark_background')

# plot show
plt.show()
