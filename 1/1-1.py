import numpy as np

t_final = 5.0 # Final time (seconds)
g = 9.81  #  gravity (m/s^2)
z_now = 0 #  Variable to hold current displacement

# Enter time interval
dt = 0.000001

# Print header
print('{0:6s}   {1:11s}   {2:11s}'.format('seconds', 'calculated', 'analytic'))

# Forward step one time
n = 0
t = n*dt  # time on entering step
z_new = z_now - dt*g*t**(1.5)
# Swap time levels
z_old = z_now  
z_now = z_new
t_new = (n+1)*dt  # time on leaving step
z_analytic = -(2.0/5.0)*g*t_new**(2.5)  # Analytic soln.

# Print results
print('{0:6.4f}  {1:11.6f}  {2:11.6f}'.format(t_new,z_now,z_analytic))

# Print header
print('{0:6s}   {1:11s}   {2:11s}'.format('seconds', 'calculated', 'analytic'))

# Main loop
for n in range(1, int(t_final/dt)): # Note:  n starts at 1, not 0
    
    #Write your code here
    t = n*dt  # time on entering step
    z_new = z_old - 2*dt*g*t**(1.5)
    z_old = z_now  
    z_now = z_new #  Swap time levels
    t_new = (n+1)*dt  # time on leaving step
    z_analytic = -(2.0/5.0)*g*t_new**(2.5)  # Analytic solution
    
    # Print results
    print('{0:6.4f}  {1:11.6f}  {2:11.6f}'.format(t_new,z_now,z_analytic))