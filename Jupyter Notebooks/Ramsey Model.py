"|===========================================================================|"
"|===========================================================================|"
"|MACROECONOMICS WITH PYTHON: A SIMPLE RAMSEY MODEL                          |"
"|Nicolas Cachanosky                                                         |"
"|Metropolitan State University of Denver                                    |"
"|ncachano@msudenver.edu                                                     |"
"|http://www.ncachanosky.com                                                 |"
"|===========================================================================|"
"|===========================================================================|"


"|***************************************************************************|"
"|CELL #1|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np              # Package for scientific computing with Python
import matplotlib.pyplot as plt # Matplotlib is a 2D plotting library


"2|DEFINE PARAMETERS AND ARRAYS"
# PARAMETERS
size    = 5        # Model domain
steps   = size*100    # Number of "dots" in the domain

# ARRAY
c = np.linspace(0, size, steps) # Create array of consumption


"3|DEFINE UTILITY FUNCTION"
# Production function
def u(x, CRRA):
    if CRRA == 1:
        u = np.log(x)
    else:
        u = ((x)**(1-CRRA)-1)/(1-CRRA)
    return u


"4|CALCULATE UTILITY FUNCTIONS FOR DIFFERENT VALUES OF THETA"
theta = [0.25, 0.75, 1, 1.5, 2]

u1 = u(c[1:], theta[0])
u2 = u(c, theta[1])
u3 = u(c, theta[2])
u4 = u(c, theta[3])
u5 = u(c, theta[4])


"5|PLOT UTILITY FUNCTIONS"
### AXIS RANGE
v = [0, size, -10, 5]    
### BUILD PLOT AND POPULIATE WITH LOCI LINES
fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(c, u1, alpha = 0.8, label = r'$\theta=%.2f$' %theta[0])
ax.plot(c, u2, alpha = 0.8, label = r'$\theta=%.2f$' %theta[1])
ax.plot(c, u3, alpha = 0.8, label = r'$\theta=%.2f$' %theta[2])
ax.plot(c, u4, alpha = 0.8, label = r'$\theta=%.2f$' %theta[3])
ax.plot(c, u5, alpha = 0.8, label = r'$\theta=%.2f$' %theta[4])
### AXIS
ax.axhline(0, color = 'k') # Add horizontal axis
ax.axvline(0, color = 'k') # Add vertical axis
ax.yaxis.set_major_locator(plt.NullLocator())                # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())                # Hide ticks
### TEXT 
plt.text(size-0.10, -0.5, r'$c$', color = 'k') # x-axis label
plt.text(    -0.25,  4.5, r'$u(c)$')           # y-axis label
# SETTINGS
plt.box(False)                                               # Hide axis
plt.legend(loc=0, frameon=False)
plt.axis(v)
plt.show()


c



"|***************************************************************************|"
"|CELL #2|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np              # Package for scientific computing with Python
import matplotlib.pyplot as plt # Matplotlib is a 2D plotting library

"2|DEFINE PARAMETERS AND ARRAYS"
# PARAMETERS
k_size  =  150        # Model domain
steps   =  k_size*100 # Number of "dots" in the domain
alpha   =  0.30       # Output elasticity of capital
delta   =  0.35       # Depreciation rate
rho     =  0.35       # Time preference
n       =  0.05       # Population growth rate
g       =  0.05       # TFP growth rate
theta   =  0.8        # Coefficient or Relative Risk Aversion
# ARRAY
k_array = np.linspace(0, k_size, steps) # Create array of k


"3|DEFINE FUNCTIONS"
# Production function
def y(k):
    y = k**alpha
    return y

# Marginal product of capital
def y_prime(k):
    y_prime = alpha*k**(alpha-1)
    return y_prime

# Consumption
def consumption(k):
    c = y(k) - (n + g + delta)*k
    return c

# Motion functino of consumption
def cdot(k, c):
    cdot = 1/theta * (y_prime(k) - delta - rho) * c
    return cdot

# Motion function of capital
def kdot(k, c):
    kdot = y(k) - c - (n + g + delta)*k 
    return kdot
    

"4|CALCULATE STEADY STATE AND GOLD VALUES"
# Steay State values
k_star = (delta + rho)**(1/alpha)
c_star = consumption(k_star)
y_star = y(k_star)
s_star = (y_star - c_star)/y_star

# Gold values
k_gold = (alpha/(n+g+delta))**(1/(1-alpha))
c_gold = consumption(k_gold)
y_gold = y(k_gold)
s_gold = (y_gold - c_gold)/y_gold


"5|CALCULATE LOCI FUNCTIONS"
k_loci = k_star
c_loci = consumption(k_array)


"6|CALCULATE SAMPLE PATHS"
k00, k01, k02 = k_star*0.25, k_star*0.50, k_star*2.2
c0 = [consumption(k00)*0.25, consumption(k00), c_star*1.25,
      consumption(k01)*0.40, consumption(k01)*1.50]

def sample_path(k0, c0, n):
    path = np.zeros(shape=(n, 2))
    path[0, 0] = k0
    path[0, 1] = c0
    
    for j in range(n-1):
        if path[j,0] < 0: # Stop if motion goes off-chart
            break
        else:
            path[j+1, 0] = path[j, 0] + kdot(path[j, 0], path[j, 1])*0.25
            path[j+1, 1] = path[j, 1] + cdot(path[j, 0], path[j, 1])*0.25
    return path

path1 = sample_path(k00, c0[0], 30)
path2 = sample_path(k00, c0[1], 30)
path3 = sample_path(k01, c0[2], 30)
path4 = sample_path(k02, c0[3], 30)
path5 = sample_path(k02, c0[4], 30)


"7|PLOT RAMSEY MODEL WITH SAMPLE PATHS"
# Value of k such that c = 0
k_zero = (1/(n + g + delta))**(1/(1-alpha))
# Axis range
y_max = np.max(c_loci)*1.7
x_max = k_zero*1.2
v = [0, x_max, -0.1, y_max]                        

### BUILD PLOT AND POPULIATE WITH LOCI LINES
fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(k_array, c_loci, color="K", alpha = 0.8)
ax.axvline(k_loci, color="K", alpha = 0.8)
### SAMPLE PATHS
ax.plot(path1[:,0], path1[:,1], "r--", alpha = 0.7)
ax.plot(path2[:,0], path2[:,1], "r--", alpha = 0.7)
ax.plot(path3[:,0], path3[:,1], "r--", alpha = 0.7)
ax.plot(path4[:,0], path4[:,1], "r--", alpha = 0.7)
ax.plot(path5[:,0], path5[:,1], "r--", alpha = 0.7)
### ADD DOTS AT BEGINNING OF SAMPLE PATHS
plt.plot(k00, c0[0], 'ro', alpha = 0.7)
plt.plot(k00, c0[1], 'ro', alpha = 0.7)
plt.plot(k01, c0[2], 'ro', alpha = 0.7)
plt.plot(k02, c0[3], 'ro', alpha = 0.7)
plt.plot(k02, c0[4], 'ro', alpha = 0.7)
### ADD MOTION ARROWS
plt.arrow(k00, c0[0], 0, 0.10, head_width=0.03,head_length=0.02,fc='r',ec='r')
plt.arrow(k00, c0[0], 0.18, 0, head_width=0.02,head_length=0.03,fc='r',ec='r')
plt.arrow(k01, c0[2], 0, 0.10, head_width=0.03,head_length=0.02,fc='r',ec='r')
plt.arrow(k01, c0[2],-0.08, 0, head_width=0.02,head_length=0.03,fc='r',ec='r')
plt.arrow(k02, c0[3], 0,-0.08, head_width=0.03,head_length=0.02,fc='r',ec='r')
plt.arrow(k02, c0[3], 0.22, 0, head_width=0.02,head_length=0.03,fc='r',ec='r')
plt.arrow(k02, c0[4], 0,-0.12, head_width=0.03,head_length=0.02,fc='r',ec='r')
plt.arrow(k02, c0[4],-0.12, 0, head_width=0.02,head_length=0.03,fc='r',ec='r')
### AXIS
ax.axvline(0, color="k")                                     # y-axis
ax.axhline(0, color="k")                                     # x-axis
ax.yaxis.set_major_locator(plt.NullLocator())                # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())                # Hide ticks
### TEXT 
plt.text(x_max*0.98, -0.05      , r'$\hat{k}$', color = 'k') # x-axis label
plt.text(-0.15 , y_max*0.95     , r'$\hat{c}$', color = 'k') # y-axis label
plt.text(k_star*1.05, y_max*0.95, r'$\hat{c}=0$', color = "k")
plt.text(k_zero*0.95, 0.07      , r'$\hat{k}=0$', color = "k")
# SETTINGS
plt.axis(v)
plt.box(False)                                               # Hide axis
plt.show()


"8|STABLE-PATH: FORWARD AND BACKWARD SHOOTING"
def forward_shoot(k0, step):
    # Set conditions for initial shoot
    tol   = 1.0e-10
    c0    = consumption(k0) - step
    error = np.abs(((k0 - k_star)**2 + (c0 - c_star)**2)**0.5)
    path      = np.zeros(shape=(1, 2))
    path[0,0] = k0
    path[0,1] = c0

    # Start loop (forward shoot)
    count = 0
    while 1:
        k1 = path[count, 0]
        c1 = path[count, 1]
        k2 = k1 + kdot(k1, c1)*0.1
        c2 = c1 + cdot(k1, c1)*0.1
        error = np.abs(((k2 - k_star)**2 + (c2 - c_star)**2)**0.5)
        path = np.append(path, [[k2, c2]], axis = 0)
        count = count + 1

        # Check if this is the stable-path
        if error < tol:
            break
        
        # Set up code break and reset the shoot
        if c2 > c_star:
            path = np.zeros(shape=(1, 2))
            c0 = c0 - step
            path[0,0] = k0
            path[0,1] = c0
            count = 0
        
        # Break code when k < k*
        if k2 > k_star:
            break
        
        # Put a limit of iterations to the code
        if count > 100:
            break
       
    return path


def backward_shoot(k0, step):
    # Set conditions for initial shoot
    tol   = 1.0e-10
    c0    = consumption(k_gold) * 1.5
    error = np.abs(((k0 - k_star)**2 + (c0 - c_star)**2)**0.5)
    path      = np.zeros(shape=(1, 2))
    path[0,0] = k0
    path[0,1] = c0

    # Start loop (forward shoot)
    count = 0
    while 1: # Infinite loop with break conditions inside
        k1 = path[count, 0]
        c1 = path[count, 1]
        k2 = k1 + kdot(k1, c1)*0.01
        c2 = c1 + cdot(k1, c1)*0.01
        error = np.abs(((k2 - k_star)**2 + (c2 - c_star)**2)**0.5)
        path = np.append(path, [[k2, c2]], axis = 0)
        count = count + 1

        # Check if this is the stable-path
        if error < tol:
            break
        
        # Set up code break and reset the shoot
        if c2 < c_star:
            path = np.zeros(shape=(1, 2))
            c0 = c0 + step
            path[0,0] = k0
            path[0,1] = c0
            count = 0
        
        # Break code when k < k*
        if k2 < k_star:
            break
        
        # Put a limit of iterations to the code
        if count > 400:
            break
       
    return path

stable_L = forward_shoot(k00, 0.000001)
stable_R = backward_shoot(k_star*2.00, 0.000001)



"9|PLOT RAMSEY MODEL WITH STABLE PATH"
# Value of k such that c = 0
k_zero = (1/(n + g + delta))**(1/(1-alpha))
# Axis range
y_max = np.max(c_loci)*1.7
x_max = k_zero*1.2
v = [0, x_max, -0.1, y_max]                        

### BUILD PLOT AND POPULIATE WITH LOCI LINES
fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(k_array, c_loci, color="K", alpha = 0.8)
ax.axvline(k_loci, color="K", alpha = 0.8)
### STABLE PATH
ax.plot(stable_L[:,0], stable_L[:,1], "b--", alpha = 0.7)
ax.plot(stable_R[:,0], stable_R[:,1], "b--", alpha = 0.7)
### AXIS
ax.axvline(0, color="k")                                     # y-axis
ax.axhline(0, color="k")                                     # x-axis
ax.yaxis.set_major_locator(plt.NullLocator())                # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())                # Hide ticks
### TEXT 
plt.text(x_max*0.98, -0.05      , r'$\hat{k}$', color = 'k') # x-axis label
plt.text(-0.15 , y_max*0.95     , r'$\hat{c}$', color = 'k') # y-axis label
plt.text(k_star*1.05, y_max*0.95, r'$\hat{c}=0$', color = "k")
plt.text(k_zero*0.95, 0.07      , r'$\hat{k}=0$', color = "k")
plt.text(k_star*1.05, -0.05     , r'$k^*$'      , color = 'k')
plt.text(-0.15, c_star          , r'$c^*$'      , color = 'k')
ax.axhline(c_star, 0, k_star/v[1], linestyle=":", color = "grey")
# SETTINGS
plt.axis(v)
plt.box(False)                                               # Hide axis
plt.show()