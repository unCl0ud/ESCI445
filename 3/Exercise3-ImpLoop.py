import numpy as np

fin = 'streamfunction_input.dat' # Input file name

psi = np.transpose(np.loadtxt(fin)) # Read data from file into NumPy array named data

# Set some parameters
dx = 5e4    #   Data spacing in meters
nx, ny = np.shape(psi)  # Determines number of data points in x and y directions

# Create arrays to hold geostrophic wind components
u = np.ndarray((nx,ny), dtype = np.float_)
u.fill(0)
v = np.copy(u)

# Write your code here
u[0:nx,1:ny-1] = -(psi[0:nx,2:ny] - psi[0:nx,0:ny-2]) / (2*dx)

# Write your code here
v[1:nx-1,0:ny] = (psi[2:nx,0:ny] - psi[0:nx-2,0:ny]) / (2*dx)

inline = False # Set False for interactive plots; True for inline plots

import matplotlib.pyplot as plt
from matplotlib import rcParams

if inline:
    rcParams['figure.figsize'] = (15, 12.0)
else:
    rcParams['figure.figsize'] = (7.5, 6.0)
    
max_s, min_s = max((np.max(u),np.max(v))), min((np.min(u),np.min(v)))

fig, ax = plt.subplots(2,1,sharex=True,sharey=True)

data = (u, v)
title = (r'$u_g$', r'$v_g$')

for i, a in enumerate(ax):
    pc = a.pcolor(np.transpose(data[i]),vmin = min_s, vmax = max_s)
    a.set_xlim(0,nx-1)
    a.set_ylim(0,ny-1)
    cb = plt.colorbar(pc,ax = a)
    cb.set_label(r'$m\/s^{-1}$', size = 'x-large')
    a.contour(np.transpose(psi), colors = 'black')
    a.set_title(title[i], size = 'xx-large')

plt.show()