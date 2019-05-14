import numpy as np
from math import pi,sin,cos,sqrt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm



# Temperature of walls [Front, Left, Right, Back]
Wfront = 31
Wleft = 13
Wright = 43
Wback = 53

#Thermal diffusivity
thermdif = 0.000099

#Time - Final run time and time step
tf = 30
dt = 0.05
#Time array is preallocated from 0 to the final time with respect to each timestep.
t = np.arange(0,tf,dt)

#Dimensions of 'box'(Length from wall to wall)
sizex = 0.5
sizey = 0.5
#Number of points between each step (divides the steps even further to create a set length and to increase resolution)
points=30
#Number of steps between walls. The length is divided into n points.
dx = sizex/points
dy = sizey/points

#x and y spatial array is created and a mesh grid is attributed to it. We use the midpoint between each point. (dx/2)
#The array will have length from the midpoint of the first value along dx/dy and a last point (before wall).
x = np.linspace(dx/2, sizex - dx/2, points)
y = np.linspace(dy/2, sizey - dy/2, points)

#A meshgrid is created using the spatial arrays above.
X,Y = np.meshgrid(x,y)

#Creation of temperature arrays/loop. 

#Temperature array is created. for loop is needed to pass x and y values through the array to compute the temperature.
#Modifying the constant before the sin function gives different intial temperatures.

Tempx = np.array([20*sin(pi*i/sizex) for i in x])
Tempy = np.array([20*sin(pi*i/sizey) for i in y])

#Meshgrid of thermal values is created.
TempX, TempY = np.meshgrid(Tempx,Tempy)

#Here empty vectors are preallocated so that the animation can be constructed. 
Animatex = np.empty(points)
Animatey = np.empty(points)

#3D plot is called from matplotlib
fig = plt.figure()
ax = fig.gca(projection='3d')


#For loop is created with the length of time. Thus it will animate for the designated time then stop.
for n in range(1,len(t)):

    ax.clear() #Previous plot is cleared

    for m in range(1,points-1): #For loop is created to iterate over the spatial domain.
        
        #Animation is utilized here. We are using the for loop to compute the derivative in order to produce the next value of temperatures.
        Animatex[m] = thermdif*((Tempx[m+1]-(2*Tempx[m])+Tempx[m-1])/dx**2)
        Animatey[m] = thermdif*((Tempy[m+1]-(2*Tempy[m])+Tempy[m-1])/dx**2)

    
    #Here we add the boundary conditions. We use the Animate function to iterate over the derivatives of values near each wall. This allows us to input the
    #temperature of the wall and allow the program to loop over each point along the grid between walls.
    Animatex[0] = thermdif*((Tempx[1]-(2*Tempx[0])+Wfront)/dx**2)
    Animatey[0] = thermdif*((Tempy[1]-(2*Tempy[0])+Wright)/dx**2)
    Animatex[points-1] = thermdif*((Wleft-(2*Tempx[points-1])+Tempx[points-2])/dx**2)
    Animatey[points-1] = thermdif*((Wback-(2*Tempy[points-1])+Tempy[points-2])/dx**2)


    #Here we use replace the temperature values in x and y. This allows the figure to refresh the final temperature meshgrid with new values.
    Tempx = Tempx + Animatex*dt
    Tempy = Tempy + Animatey*dt
    TempX, TempY = np.meshgrid(Tempx,Tempy)

    #The results from the temperature meshgrid are both set equal to the variable T (temperature). This is the z-axis in the plot. 
    T = (TempX + TempY)
    
    #Surf takes in the the arrays X,Y, and T and maps it to a 3D figure.
    surf = ax.plot_surface(X,Y,T, cmap=cm.bwr,
                           linewidth=0, antialiased = False)
    
    #Axis limitations are set.
    ax.set_zlim(0,120)
    ax.set_xlim(0,0.5)
    ax.set_ylim(0,0.5)
    
    #Axis labels are created
    ax.set_xlabel('Distance (meters)')
    ax.set_ylabel('Distance (meters)')
    ax.set_zlabel('Temperature (C)')
    
    #Figure is created.
    plt.show()
    plt.pause(0.001)