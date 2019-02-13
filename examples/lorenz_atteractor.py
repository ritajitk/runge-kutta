from pylab import *
from rk import RK4
from mpl_toolkits.mplot3d import Axes3D

s=10; r=28; b=2.667
x_dot = lambda t,y,x,z : s*(y - x)
y_dot = lambda t,y,x,z : r*x - y - x*z
z_dot = lambda t,y,x,z : x*y - b*z
lor = RK4(y_dot,x_dot,z_dot)
t,y = lor.solve([1., 0., 1.05],0.01,100)
fig = figure()
ax = fig.gca(projection='3d')

ax.plot(y[0],y[1],y[2],lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

show()
