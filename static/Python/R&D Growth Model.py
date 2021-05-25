#|============================================================================|
#|============================================================================|
#|MACROECONOMICS WITH PYTHON: THE R&D GROWTH MODEL                            |
#|Nicolas Cachanosky                                                          |
#|Metropolitan State University of Denver                                     |
#|ncachano@msudenver.edu                                                      |
#|http://www.ncachanosky.com                                                  |
#|============================================================================|
#|============================================================================|

#%% *** CELL 1 ***
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library


"|***************************************************************************|"
"2|DEFINE PARAMETERS AND ARRAYS"
# Code parameters
dpi = 300
step  = 0.01
# Model parameters
n     = 0.02      # Growth rate of population
beta  = 0.50      # Exponent of capital in the production of ideas
gamma = 1 - beta  # Exponent of labor in the priduction of ideas
theta = 0.25      # Exponent of technology in the production of ideas

# Arrays
gA = np.arange(0, 1, step) # Array between 0 and 1 with step size=0.01
gK = n + gA


"|***************************************************************************|"
"3|DEFINE AND POPULATE THE SADDLE-PATH FUNCTIONS" 
# Saddle paths for K and A
ss_K = n + gA
ss_A = -(gamma*n)/beta + (1 - theta)/beta*gA

# Intercept of K saddle-path
ss_int = -(gamma*n)/beta


"|***************************************************************************|"
"4|EQUILIBRIUM VALUES"
A_star = n*(beta + gamma)/(1 - (theta + gamma))
K_star = n + A_star


"|***************************************************************************|"
"5|PLOT THE SADDLE-PATH"
### AXIS RANGE
axis_range = [0, gA.max()*0.2, -0.05, gK.max()*0.2]

### BUILD FIGURE
plt.figure(figsize=(10, 7), dpi=dpi)
plt.title("DYNAMICS OF GROWTH RATES OF CAPITAL AND TECHNOLOGY")
plt.plot(gA, ss_A, "k-", label=r'$g_A(t)$')
plt.plot(gA, ss_K, "k-", label=r'$g_K(t)$')
### EQUILIBRIUM MARKS
plt.axvline(A_star, -axis_range[2]/(0.25), (0.05+K_star)/0.25  , ls=":")
plt.axhline(K_star, 0.0                  , A_star/axis_range[1], ls=":")
### AXIS
plt.axvline(0, color="k")  # Add vertical axis
plt.axhline(0, color="k")  # Add horizontal axis
plt.xticks([], [])         # Hide x-axis ticks
plt.yticks([], [])         # Hide y-axis ticks
plt.text(-0.01             , axis_range[3]-0.01, r'$g_K(t)$')  # x-axis label
plt.text(axis_range[1]-0.01, -0.01             , r'$g_A(t)$')  # y-axis label
### VALUES AND LABELS
plt.text(axis_range[1]-0.03, axis_range[3]-0.02, r'$\dot{g_A(t)^*}=0$')
plt.text(axis_range[1]-0.09, axis_range[3]-0.02, r'$\dot{g_K(t)^*}=0$')
plt.text(A_star, -0.01 , r'$g_A(t)^*$', horizontalalignment="center")
plt.text(-0.001, K_star, r'$g_K(t)^*$', horizontalalignment="right")
plt.text(-0.001, n     , r'$n$'       , horizontalalignment="right")
plt.text(-0.001, ss_int, r'$-\frac{\gamma n}{\beta}$',
         horizontalalignment="right")
### SETINGS
plt.box(False)
plt.axis(axis_range)
plt.show()


#%% *** CELL 2 ***
"|***************************************************************************|"
"6|DEFINE PARAMETERS AND ARRAYS"
# Parameters
alpha = 0.60  # Exponent of capital in the production of goods


"|***************************************************************************|"
"7|STABILITY DYNAMICS"
iterations = 75

" | Starting Poin A (blue)"
# Create arrays to store model dynamics
A_gA = np.zeros(iterations)
A_gK = np.zeros(iterations)
# Set arbitrary initial values
A_gA[0] = 0.015                                  
A_gK[0] = 0.020                                  

for j in range(1, iterations):
    A_gA[j] = A_gA[j-1] + beta*A_gK[j-1] + gamma*n + (theta-1)*A_gA[j-1]
    A_gK[j] = A_gK[j-1] + (1-alpha)*(A_gA[j-1] + n - A_gK[j-1])

" | Starting Poin B (green)"
# Create arrays to store model dynamics
B_gA = np.zeros(iterations)
B_gK = np.zeros(iterations)
# Set arbitrary initial values
B_gA[0] = 0.015
B_gK[0] = 0.180

for j in range(1, iterations):
    B_gA[j] = B_gA[j-1] + beta*B_gK[j-1] + gamma*n + (theta-1)*B_gA[j-1]
    B_gK[j] = B_gK[j-1] + (1-alpha)*(B_gA[j-1] + n - B_gK[j-1])

" | Starting Poin C (red)"
# Create arrays to store model dynamics
C_gA = np.zeros(iterations)
C_gK = np.zeros(iterations)
# Set arbitrary initial values
C_gA[0] = 0.150
C_gK[0] = 0.180

for j in range(1, iterations):
    C_gA[j] = C_gA[j-1] + beta*C_gK[j-1] + gamma*n + (theta-1)*C_gA[j-1]
    C_gK[j] = C_gK[j-1] + (1-alpha)*(C_gA[j-1] + n - C_gK[j-1])

" | Starting Poin D (cyan)"
# Create arrays to store model dynamics
D_gA = np.zeros(iterations)
D_gK = np.zeros(iterations)
# Set arbitrary initial values
D_gA[0] = 0.150
D_gK[0] = 0.020

for j in range(1, iterations):
    D_gA[j] = D_gA[j-1] + beta*D_gK[j-1] + gamma*n + (theta-1)*D_gA[j-1]
    D_gK[j] = D_gK[j-1] + (1-alpha)*(D_gA[j-1] + n - D_gK[j-1])


"|***************************************************************************|"
"8|PLOT THE SADDLE-PATH"
### AXIS RANGE
axis_range = [0, gA.max()*0.2, -0.05, gK.max()*0.2]

# BUILD PLOT
plt.figure(figsize=(10, 7), dpi=dpi)
plt.title("MODEL STABILITY")
plt.plot(gA, ss_A, "k-", label=r'$g_A(t)$')
plt.plot(gA, ss_K, "k-", label=r'$g_K(t)$')
### EQUILIBRIUM MARKS
plt.axvline(A_star, -axis_range[2]/(0.25), (0.05+K_star)/0.25  , ls=":")
plt.axhline(K_star, 0.0                  , A_star/axis_range[1], ls=":")
### AXIS
plt.axvline(0, color="k")  # Add vertical axis
plt.axhline(0, color="k")  # Add horizontal axis
plt.xticks([], [])         # Hide x-axis ticks
plt.yticks([], [])         # Hide y-axis ticks
plt.text(-0.01              , axis_range[3]-0.01, r'$g_K(t)$')  # x-axis label
plt.text(axis_range[1]-0.01, -0.01              , r'$g_A(t)$')  # y-axis label
### VALUES AND LABELS
plt.text(A_star, -0.01 , r'$g_A(t)^*$', horizontalalignment="center")
plt.text(-0.001, K_star, r'$g_K(t)^*$', horizontalalignment="right")
plt.text(axis_range[1]-0.03, axis_range[3]-0.02, r'$\dot{g_A(t)^*}=0$')
plt.text(axis_range[1]-0.09, axis_range[3]-0.02, r'$\dot{g_K(t)^*}=0$')
### MODEL DYNAMICS
plt.plot(A_gA[0], A_gK[0], "bo")
plt.plot(A_gA   , A_gK   , "b:")
plt.plot(B_gA[0], B_gK[0], "go")
plt.plot(B_gA   , B_gK   , "g:")
plt.plot(C_gA[0], C_gK[0], "ro")
plt.plot(C_gA   , C_gK   , "r:")
plt.plot(D_gA[0], D_gK[0], "co")
plt.plot(D_gA   , D_gK   , "c:")
plt.text(A_gA[0]-0.005, A_gK[0]      , "A", color="b")
plt.text(B_gA[0]-0.005, B_gK[0]      , "B", color="g")
plt.text(C_gA[0]      , C_gK[0]+0.005, "C", color="r")
plt.text(D_gA[0]+0.005, D_gK[0]      , "D", color="c")
# ARROWS
plt.arrow(A_gA[0], A_gK[0],  0.005, 0    , color="b")
plt.arrow(A_gA[0], A_gK[0],  0    , 0.005, color="b")
plt.arrow(B_gA[0], B_gK[0],  0.005, 0    , color="g")
plt.arrow(B_gA[0], B_gK[0],  0    ,-0.005, color="g")
plt.arrow(C_gA[0], C_gK[0], -0.005, 0    , color="r")
plt.arrow(C_gA[0], C_gK[0],  0    ,-0.005, color="r")
plt.arrow(D_gA[0], D_gK[0], -0.005, 0    , color="c")
plt.arrow(D_gA[0], D_gK[0],  0    , 0.005, color="c")
### SETTINGS
plt.box(False)
plt.axis(axis_range)
plt.show()