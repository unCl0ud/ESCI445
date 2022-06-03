import matplotlib.pyplot as plt  # Import matplotlib pyplot aliased to plt
import numpy as np  # Import numerical python aliased to np
from matplotlib import rcParams

dx = 1e3  #  Grid spacing in meters
dt = 30  # Time interval in seconds
nx = 601   #  Number of grid points
n_total = 500  # Final time index at end of simulation
n_save = 10   #  Number of iterations between saves
x = np.arange(0,nx)*dx/1000.0  #  Grid values (in kilometers)

width = 20   #  Signal width in grid points
c = 15   # Speed of wave in meters per second

u_now = np.zeros(nx, dtype = np.float_)  #  Value at current time step
u_next = np.zeros_like(u_now)  #  Value at next time step
u = np.zeros((0, nx), dtype = np.float_)  # define a variable to hold the output values

Gaussian = False  # If true, initial data is Gaussian.  Otherwise, it is rectangel

if Gaussian:
    std = 6.0  # number of gridpoints for standard deviation
    arg = ((nx/2-np.arange(0,nx))**2)/(4*std**2)
    u_now[0:nx] = np.exp(-arg)
else:
    width = 20   #  Signal width
    start, stop = int(nx/2) - int(width/2), int(nx/2) + int(width/2)
    u_now[start:stop] = 1.0

u = np.vstack((u, u_now))    #  Saves initial data for output

sigma = c*dt/dx  # Defined here so it isn't in the loop

for n in range(0, n_total): # start of time loop
    
    # Write your code here to loop through the grid
    for i in range(1,nx):
        u_next[i] = u_now[i] - sigma * (u_now[i] - u_now[i-1])

    #Swap the vars
    u_now = np.copy(u_next)

    # Prints out amplitude of signal
    print(n+1, np.max(abs(u_now)))
    
    # Save output
    if (n+1) % n_save == 0:
        u = np.vstack((u, u_now))

np.save('fit-bis', u) # Saves output as NumPy array file

inline = False  # True for inline plot, False for interactive
    
s = r'$u^{' + str(n_total) + r'}$'
plt.plot(x, u[0,:], 'g-',label = r'$u^0$')
plt.plot(x, u[-1,:], 'b-',label = s)
plt.xlim(x[0],x[-1])
umin, umax = np.min(u), np.max(u)
plt.ylim(umin-0.2, umax+0.2)

# Create actual solution for comparison
displacement = c*dt*n_total  # distance signal is displaced
nindex = int(displacement/dx)  # number of grid points signal is displaced
plt.plot(x, np.roll(u[0,:], nindex), 'r:', label = r'$Analytic$')

plt.legend((r'$u^0$', s, r'$Analytic$'), loc = 0)
plt.show()
