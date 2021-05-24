#|============================================================================|
#|============================================================================|
#|MACROECONOMICS WITH PYTHON: THE IS-LM MODEL                                 |
#|Nicolas Cachanosky                                                          |
#|Metropolitan State University of Denver                                     |
#|ncachano@msudenver.edu                                                      |
#|http://www.ncachanosky.com                                                  |
#|============================================================================|
#|============================================================================|

#%% *** CELL 1 ***
"============================================================================"
"1|IMPORT PACKAGES"
import numpy             as np   # Package for scientific computing
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library


"============================================================================"
"2|DEFINE PARAMETERS AND ARRAYS"
# Code parameters
dpi = 300
# IS parameters
Y_size = 100
a      =  20    # Autonomous consumption
b      =   0.2  # Marginal propensity to consume
alpha  =   5    # Autonomous imports
beta   =   0.2  # Marginal propensity to import
T      =   1    # Taxes
I      =  10    # Investment intercept (when i = 0)
G      =   8    # Government spending
X      =   2    # Exports (given)
d      =   5    # Investment slope wrt to i
# Arrays
Y = np.linspace(0, Y_size, Y_size*2)  # Array values of Y


"============================================================================"
"3|DEFINE AND POPULATE THE IS-SCHEDULE"
def i_IS(a, alpha, b, beta, T, I, G, X, d, Y):
    i_IS = ((a-alpha)-(b-beta)*T + I + G + X - (1-b+beta)*Y)/d
    return i_IS

def Y_IS(a, alpha, b, beta, T, I, G, X, d, i):
    Y_IS = ((a-alpha)-(b-beta)*T + I + G + X - d*i)/(1-b+beta)
    return Y_IS

i = i_IS(a, alpha, b, beta, T, I, G, X, d, Y)


"============================================================================"
"4|PLOT THE IS-SCHEDULE"
### AXIS RANGE
y_max = np.max(i)
x_max = Y_IS(a, alpha, b, beta, T, I, G, X, d, 0)
axis_range = [0, x_max, 0, y_max]                        

### BUILD PLOT
fig, ax = plt.subplots(figsize=(10, 8), dpi=dpi)
ax.set(title="IS SCHEDULE", xlabel=r'Y', ylabel=r'r')
ax.plot(Y, i, "k-")
### AXIS
ax.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
### SETTINGS
plt.axis(axis_range)
plt.show()


#%% *** CELL 2 ***
"============================================================================"
"5|DEFINE PARAMETERS"
# LM Parameters
c1 = 1000       # Precautionary money demand
c2 = 10         # Transaction money demand
c3 = 10         # Speculation money demand
Ms = 20000      # Nominal money supply
P  = 20         # Price level


"============================================================================"
"6|DEFINE AND POPULATE THE LM-SCHEDULE"
def i_LM(c1, c2, c3, Ms, P, Y):
    i_LM = (c1 - Ms/P)/c3 + c2/c3*Y
    return i_LM

i = i_LM(c1, c2, c3, Ms, P, Y)


"============================================================================"
"7|PLOT THE LM-SCHEDULE"
### AXIS RANGE
y_max = np.max(i)
axis_range = [0, Y_size, 0, y_max]

### BUILD PLOT
fig, ax = plt.subplots(figsize=(10, 8), dpi=dpi)
ax.set(title="LM SCHEDULE", xlabel=r'Y', ylabel=r'r')
ax.plot(Y, i, "k-")
ax.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
### SETTINGS
plt.axis(axis_range)
plt.show()


#%% *** CELL 3 ***
"============================================================================"
"8|DEFINE NEW PARAMETERS"
# IS new parameters
a = 100              # Autonomous consumption
b = 0.2              # Marginal propensity to consume
alpha = 5            # Autonomous imports
beta  = 0.15         # Marginal propensity to import
T = 1                # Taxes
I = 10               # Investment intercept (when i = 0)
G = 20               # Government spending
X = 5                # Exports (given)
d = 2                # Investment slope wrt to i
# LM new parameters
c1 = 2500            # Precautionary money demand
c2 = 0.75            # Transaction money demand
c3 = 5               # Speculation money demand
Ms = 23500           # Nominal money supply
P  = 10              # Price level


"============================================================================"
"9|CALCULATE EQUILIBRUM VALUES"

iIS = i_IS(a, alpha, b, beta, T, I, G, X, d, Y)
iLM = i_LM(c1, c2, c3, Ms, P, Y)

Y_star1 = ((a-alpha) - (b-beta)*T + I + G + X)/d
Y_star2 = (1/c3) * (c1 - Ms/P)
Y_star3 = (1 - b + beta)/d + (c2/c3)
Y_star  = (Y_star1 - Y_star2)/Y_star3

i_star1 = (1/c3)*(c1 - Ms/P)
i_star2 = (c2/c3)*Y_star
i_star  = i_star1 + i_star2


"============================================================================"
"10|PLOT THE IS-LM model"
### AXIS RANGE
y_max = np.max(iIS)
axis_range = [0, Y_size, 0, y_max]

### BUILD PLOT
fig, ax = plt.subplots(figsize=(10, 8), dpi=dpi)
ax.set(title="IS-LM MODEL", xlabel=r'Y', ylabel=r'r')
ax.plot(Y, iIS, "b-")
ax.plot(Y, iLM, "r-")
### AXIS
ax.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())  # Hide ticks
### ARROWS AND EQUILIBRIUM POINT
ax.arrow(25, i_star, 10,  0, head_length=2, head_width=1, color='b', alpha=0.7)
ax.arrow(25, i_star,  0, -2, head_length=2, head_width=1, color='r', alpha=0.7)
ax.arrow(Y_star, 20, 10,  0, head_length=2, head_width=1, color='b', alpha=0.7)
ax.arrow(Y_star, 20,  0, 10, head_length=2, head_width=1, color='r', alpha=0.7)
ax.arrow(85, i_star,-10,  0, head_length=2, head_width=1, color='b', alpha=0.7)
ax.arrow(85, i_star,  0,  2, head_length=2, head_width=1, color='r', alpha=0.7)
ax.arrow(Y_star, 55,-10,  0, head_length=2, head_width=1, color='b', alpha=0.7)
ax.arrow(Y_star, 55,  0,-10, head_length=2, head_width=1, color='r', alpha=0.7)
plt.plot(Y_star, i_star, 'ko')                      # Equilibrium point
plt.axvline(x=Y_star, ls=':', color='k', alpha=0.5) # Equilibrium line
plt.axhline(y=i_star, ls=':', color='k', alpha=0.5) # Equilibrium line
### LABELS
plt.text(95, 16, "IS", color='b')
plt.text(95, 47, "LM", color='r')
### SETTINGS
plt.axis(axis_range)
plt.show()


#%% *** CELL 4 ***
"============================================================================"
"11|CALCULATE THE DYNAMICS FOR DISEQUILIBRIUM POINTS"
iterations= 10

" |STARTING POINT A"
YA, iA = 10, 50   # Initial values

A_i_LM = np.zeros(iterations)
A_Y_IS = np.zeros(iterations)

A_Y_IS[0] = YA
A_i_LM[0] = iA

for j in range(1, iterations):
    A_Y_IS[j] = Y_IS(a, alpha, b, beta, T, I, G, X, d, A_i_LM[j-1])
    A_i_LM[j] = i_LM(c1, c2, c3, Ms, P, A_Y_IS[j-1])
    
" |STARTING POINT B"
YB, iB = 80, 55   # Initial values

B_i_LM = np.zeros(iterations)
B_Y_IS = np.zeros(iterations)

B_Y_IS[0] = YB
B_i_LM[0] = iB

for j in range(1, iterations):
    B_Y_IS[j] = Y_IS(a, alpha, b, beta, T, I, G, X, d, B_i_LM[j-1])
    B_i_LM[j] = i_LM(c1, c2, c3, Ms, P, B_Y_IS[j-1])   
    
" |STARTING POINT C"
YC, iC = 70, 20   # Initial values

C_i_LM = np.zeros(iterations)
C_Y_IS = np.zeros(iterations)

C_Y_IS[0] = YC
C_i_LM[0] = iC

for j in range(1, iterations):
    C_Y_IS[j] = Y_IS(a, alpha, b, beta, T, I, G, X, d, C_i_LM[j-1])
    C_i_LM[j] = i_LM(c1, c2, c3, Ms, P, C_Y_IS[j-1])    

" |STARTING POINT D"
YD, iD = 30, 25   # Initial values

D_i_LM = np.zeros(iterations)
D_Y_IS = np.zeros(iterations)

D_Y_IS[0] = YD
D_i_LM[0] = iD

for j in range(1, iterations):
    D_Y_IS[j] = Y_IS(a, alpha, b, beta, T, I, G, X, d, D_i_LM[j-1])
    D_i_LM[j] = i_LM(c1, c2, c3, Ms, P, D_Y_IS[j-1])


"============================================================================"
"12|PLOT THE IS-LM model"
### AXIS RANGE
y_max = np.max(iIS)
axis_range = [0, Y_size, 0, y_max]

### BUILD FIGURE
fig, ax = plt.subplots(figsize=(10, 8), dpi=dpi)
ax.set(title="IS-LM MODEL", xlabel=r'Y', ylabel=r'r')
ax.plot(Y, iIS, "k-")
ax.plot(Y, iLM, "k-")
### EQUILIBRIUM POINT AND LINES
ax.plot(Y_star, i_star, "ko")
ax.axvline(x=Y_star, ls=':', color='k')
ax.axhline(y=i_star, ls=':', color='k')
### DYNAMICS
ax.plot(YA, iA, "bo")                     # Starting point A
ax.plot(A_Y_IS, A_i_LM, "b--", alpha=0.7)
ax.plot(YB, iB, "ro")                     # Starting point B
ax.plot(B_Y_IS, B_i_LM, "r--", alpha=0.7)
ax.plot(YC, iC, "go")                     # Starting point C
ax.plot(C_Y_IS, C_i_LM, "g--", alpha=0.7)
ax.plot(YD, iD, "co")                     # Starting point C
ax.plot(D_Y_IS, D_i_LM, "c--", alpha=0.7)
### LABELS
ax.text(95, 14, "IS")
ax.text(95, 47, "LM")
ax.text(YA-3, iA+1, "A", color="b")
ax.text(YB+3, iB  , "B", color="r")
ax.text(YC-3, iC  , "C", color="g")
ax.text(YD  , iD-3, "D", color="c")
### AXIS
ax.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
### SETTINGS
plt.axis(axis_range)
plt.show()