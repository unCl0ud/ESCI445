import numpy as np

fin = 'exercise_2_input.dat' # Input file name

y = np.loadtxt(fin)    # Read data from file into NumPy array named data

# Set some parameters
dx = 2.0    #   Data spacing
nx = len(y)  # Determines number of data points

wave_length = 200.0
k = 2*np.pi/wave_length  # Wavenumber
x = dx*np.arange(0,nx)  #  X values for calculating analytic derivative
analytic = k*np.cos(k*x)  # Analytic derivative

forward = np.zeros_like(analytic) # forward
forward.fill(None)  # fill it with None
backward = np.copy(forward)  # backward
centered = np.copy(forward)  # centered
fourth = np.copy(forward)    # fourth-order

#Calculate Forward difference
for i in range(0, nx-1):
    forward[i] = (y[i+1] - y[i])/dx

#Calc backward difference
for i in range(1, nx-1):
    backward[i] = (y[i] - y[i-1])/dx

#Calculate centered difference
for i in range(1, nx-1): # Note:  n starts at 1, not 0
    centered[i] = (y[i+1] - y[i-1])/(2*dx)

#Fourth-order difference
for i in range(2, nx-2):
    fourth[i] = (4.0/3.0) * ((y[i+1] - y[i-1])/(2*dx)) \
        - (1.0/3.0) * ((y[i+2] - y[i-2]) / (4*dx))

# Print results
s = '{0:3s}  {1:12s}  {2:12s}  {3:12s}  {4:12s}  {5:12s}'\
    .format(' ', ' analytic', ' forward', ' backward', ' centered', ' 4th-order')
print(s)
for i, a in enumerate(analytic):
    s = '{0:3d}  {1:12.9f}  {2:12.9f}  {3:12.9f}  {4:12.9f}  {5:12.9f}'\
        .format(i,a,forward[i],backward[i],centered[i],fourth[i])
    print(s)
