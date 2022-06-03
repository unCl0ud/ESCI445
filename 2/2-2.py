import numpy as np

fin = './exercise_2_input.dat' # Input file name

y = np.loadtxt(fin)    # Read data from file into NumPy array named data

# Set some parameters
dx = 2.0    #   Data spacing
nx = len(y)  # Determines number of data points

wave_length = 200.0
k = 2*np.pi/wave_length  # Wavenumber
x = dx*np.arange(0,nx)  #  X values for calculating analytic derivative
analytic = -(k**2)*np.sin(k*x)  # Analytic derivative

second = np.zeros_like(analytic) # forward
second.fill(None)
fourth = np.copy(second)    # fourth-order

#Calculate standard difference
for i in range(1, nx-1): # Note:  n starts at 1, not 0
    second[i] = (y[i+1]+y[i-1]-2*y[i])/(dx**2)

#Calculate fourth-order difference
for i in range(2, nx-2):
    fourth[i] = (1/dx**2)*(((4/3)*(y[i+1] + y[i-1])) - ((1/12) * (y[i+2] + y[i-2])) - ((5/2) * y[i]))

# Print results
s = '{0:3s}  {1:12s}  {2:12s}  {3:12s}'.format(' ', ' analytic',' second', ' fourth')
print(s)
for i, a in enumerate(analytic):
    s = '{0:3d}  {1:12.9f}  {2:12.9f}  {3:12.9f}'.format(i,a,second[i],fourth[i])
    print(s)