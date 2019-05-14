#FinalCode-TravelingWave- MShah - 05112019 - Wave propagation and the wave equation.

#Import the proper packets needed.
import numpy as np
from numpy import pi,sin,cos,sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

#Wave Parameters
speed = 1000     #Wave Speed
fx = 3   #Wave Frequency in X
fy = 3   #Wave Frequency in Y
u = 1.5
w = 1.5
#Time Parameters
ts = .08      #Time Step
ti = 0         #Initial Time Preallocated   

#Equations

#Nested function - Omega Frequency
freq = sqrt(fx**2+fy**2) * speed * pi                                     #Omega Frequency Value
#Wave function (defined to be called later)
def wave(x,y,t):                                                          #Defining the wave function
    #return (sin(pi*fx*x) * sin(fy*pi*y) * (cos(freq*t) + sin(freq*t)))+(sin(pi*fx*x) * sin(fy*pi*y) * (cos(freq*t) + sin(freq*t)))    #Defined function for the standing wave [Midterm]  
    return ((1/sqrt(fx**2+fy**2))*(sin(u*x+w*t))) + ((1/sqrt(fx**2+fy**2))*(sin(u*y+w*t)))                                             #Defined function for traveling wave [Final]
#Construction of vectors and meshgrid
x = np.linspace(-5,5,75)     #x vector created
y = np.linspace(-5,5,75)     #y vector created

#Meshgrid construction 
X,Y = np.meshgrid(x,y)   #Grid created with size x by y.    
   
d = []               #Empty data vector pre-allocated
for r in range(500):    #For loop used to set range for animation
    c = wave(X,Y,ti)    #Wave equation defined as single variable
    ti = ti + ts        #ti is allowed to change value for each time step to compute the next point
    d.append(c)  #Append adds a value to the end of the list in the c variable (developing c as a function of time)
#Figure plotted using fig variable so it can be animated later

fig = plt.figure()

#Type of figure is set
plot = fig.gca(projection='3d')

#Size of the figure is set
fig.set_dpi(100)

#Color bar and animation is created.
color = plt.cm.ScalarMappable(cmap=plt.cm.seismic)
color.set_array(d[0])
cbar = plt.colorbar(color,label='Wave Amplitude (E)')

p = 0 #Preallocation of p variable for animation

#Definition of timeevolution animation is created with dependency on r.
#Plotting of the meshgrid surface is done. rstride and cstride creates an equal color distribution. Color is added
#linewidth and antialiasing affect the display of the figure.
def timeevolution(r):
    global p       #Calls p from outside the user defined function
    Z = d[p]       #Z parameter is set equal to the value the data at location p in the array.
    p += 1         #The position of the data value is changed
    plot.clear()     #Previous plots are cleared.
    plot.plot_surface(X,Y,Z,label='Wave Function', rstride=1, cstride=1,cmap=plt.cm.seismic,linewidth=0,antialiased=False)
    plot.contour(X,Y,Z)   #Contour lines are added
    plot.set_zlim(0,4)    #Size of the z axis is created
    plot.set_xlabel('X-Position (m)')
    plot.set_ylabel('Y-Position (m)')
    plot.set_zlabel('Wave Amplitude (m)')

#Plotting of the meshgrid surface is done. rstride and cstride creates an equal color distribution. Color is added
#linewidth and antialiasing affect the display of the figure.
#Animations are created based on the figure and the defined animation function.
anim = animation.FuncAnimation(fig,timeevolution,frames = 500)
plt.show()