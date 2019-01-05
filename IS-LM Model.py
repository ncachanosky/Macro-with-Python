"|===========================================================================|"
"|===========================================================================|"
"|MACROECONOMICS WITH PYTHON: IS-LM MODEL                                    |"
"|Nicolas Cachanosky                                                         |"
"|Metropolitan State University of Denver                                    |"
"|ncachano@msudenver.edu                                                     |"
"|http://www.ncachanosky.com                                                 |"
"|===========================================================================|"
"|===========================================================================|"

#%%
"|***************************************************************************|"
"|CELL #1|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library

"2|DEFINE PARAMETERS AND ARRAYS"
# Parameters
Y_size = 100
a = 20                 # Autonomous consumption
b = 0.2                # Marginal propensity to consume
alpha = 5              # Autonomous imports
beta  = 0.2            # Marginal propensity to import
T = 1                  # Taxes
I_bar = 10             # Investment intercept (when i = 0)
G_bar = 8              # Government spending
X_bar = 2              # Exports (given)
d = 5                  # Investment slope wrt to i
# Arrays
Y = np.arange(Y_size)  # Array values of Y
i = np.zeros(Y_size)   # Empty array of i

"3|DEFINE AND POPULATE THE IS-SCHEDULE"
def i_IS(a, alpha, b, beta, T, I_bar, G_bar, X_bar, d, Y):
    i_IS = ((a-alpha)-(b-beta)*T + I_bar + G_bar + X_bar - (1-b+beta)*Y)/d
    return i_IS

def Y_IS(a, alpha, b, beta, T, I_bar, G_bar, X_bar, d, i):
    Y_IS = ((a-alpha)-(b-beta)*T + I_bar + G_bar + X_bar - d*i)/(1-b+beta)
    return Y_IS

for j in range(0, Y_size):
    i[j] = i_IS(a, alpha, b, beta, T, I_bar, G_bar, X_bar, d, j)
    
"4|PLOT THE IS-SCHEDULE"
y_max = np.max(i)
x_max = Y_IS(a, alpha, b, beta, T, I_bar, G_bar, X_bar, d, 0)

v = [0, x_max, 0, y_max]                        # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="IS SCHEDULE", xlabel=r'Y', ylabel=r'r')
ax.plot(Y, i, "k-")
ax.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
plt.axis(v)                                     # Use 'v' as the axes range
plt.show()



#%%
"|***************************************************************************|"
"|CELL #2|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library

"2|DEFINE PARAMETERS AND ARRAYS"
# Parameters
Y_size = 100
c1 = 1000              # Precautionary money demand
c2 = 10                # Transaction money demand
c3 = 10                # Speculation money demand
Ms = 20000             # Nominal money supply
P  = 20                # Price level
# Arrays
Y = np.arange(Y_size)  # Array values of Y
i = np.zeros(Y_size)   # Empty array of i

"3|DEFINE AND POPULATE THE LM-SCHEDULE"
def i_LM(c1, c2, c3, Ms, P, Y):
    i_LM = (c1 - Ms/P)/c3 + c2/c3*Y
    return i_LM

for j in range(0, Y_size):
    i[j] = i_LM(c1, c2, c3, Ms, P, j)
    
"4|PLOT THE IS-SCHEDULE"
y_max = np.max(i)

v = [0, Y_size, 0, y_max]                       # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="LM SCHEDULE", xlabel=r'Y', ylabel=r'r')
ax.plot(Y, i, "k-")
ax.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
plt.axis(v)                                     # Use 'v' as the axes range
plt.show()



#%%
"|***************************************************************************|"
"|CELL #3|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library

"2|DEFINE PARAMETERS AND ARRAYS"
# Model domain
Y_size = 100
Y   = np.arange(Y_size)     # Array values of Y
iIS = np.zeros(Y_size)      # Empty array for the IS
iLM = np.zeros(Y_size)      # Empty array for the LM
# IS Parameters
a = 100                     # Autonomous consumption
b = 0.2                     # Marginal propensity to consume
alpha = 5                   # Autonomous imports
beta  = 0.15                # Marginal propensity to import
T = 1                       # Taxes
I = 10                      # Investment intercept (when i = 0)
G = 20                      # Government spending
X = 5                       # Exports (given)
d = 2                       # Investment slope wrt to i
# LM Parameters
c1 = 2500                   # Precautionary money demand
c2 = 0.75                   # Transaction money demand
c3 = 5                      # Speculation money demand
Ms = 23500                  # Nominal money supply
P  = 10                     # Price level

"3|DEFINE AND POPULATE THE IS AND LM SCHEDULES"
def i_IS(a, alpha, b, beta, T, I, G, X, d, Y):
    i_IS = ((a-alpha)-(b-beta)*T + I + G + X - (1-b+beta)*Y)/d
    return i_IS

def i_LM(c1, c2, c3, Ms, P, Y):
    i_LM = (c1 - Ms/P)/c3 + c2/c3*Y
    return i_LM

for j in range(0, Y_size):
    iIS[j] = i_IS(a, alpha, b, beta, T, I, G, X, d, j)
    iLM[j] = i_LM(c1, c2, c3, Ms, P, j)

"4|CALCULATE EQUILIBRUM VALUES"
Y_star1 = ((a-alpha) - (b-beta)*T + I + G + X)/d
Y_star2 = (1/c3) * (c1 - Ms/P)
Y_star3 = (1 - b + beta)/d + (c2/c3)
Y_star  = (Y_star1 - Y_star2)/Y_star3

i_star1 = (1/c3)*(c1 - Ms/P)
i_star2 = (c2/c3)*Y_star
i_star  = i_star1 + i_star2

"5|PLOT THE IS-LM model"
y_max = np.max(iIS)
v = [0, Y_size, 0, y_max]                      # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="IS-LM MODEL", xlabel=r'Y', ylabel=r'r')
ax.plot(Y, iIS, "b-")
ax.plot(Y, iLM, "r-")
ax.yaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())  # Hide ticks
ax.arrow(10, i_star, 10,  0, head_length=2, head_width=1, color='b', alpha=0.7)
ax.arrow(10, i_star,  0, -3, head_length=2, head_width=1, color='r', alpha=0.7)
ax.arrow(Y_star, 15, 10,  0, head_length=2, head_width=1, color='b', alpha=0.7)
ax.arrow(Y_star, 15,  0, 10, head_length=2, head_width=1, color='r', alpha=0.7)
ax.arrow(90, i_star,-10,  0, head_length=2, head_width=1, color='b', alpha=0.7)
ax.arrow(90, i_star,  0,  2, head_length=2, head_width=1, color='r', alpha=0.7)
ax.arrow(Y_star, 60,-10,  0, head_length=2, head_width=1, color='b', alpha=0.7)
ax.arrow(Y_star, 60,  0,-10, head_length=2, head_width=1, color='r', alpha=0.7)
plt.plot(Y_star, i_star, 'ko')                # Equilibrium point
plt.axvline(x=Y_star, ls=':', color='k')
plt.axhline(y=i_star, ls=':', color='k')
plt.text(95, 22, "IS", color='b')
plt.text(95, 47, "LM", color='r')
plt.axis(v)                                   # Use 'v' as the axes range
plt.show()



"|***************************************************************************|"
"|CELL #3|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library

"2|DEFINE PARAMETERS AND ARRAYS"
# Model domain
Y_size = 100
Y   = np.arange(Y_size)     # Array values of Y
iIS = np.zeros(Y_size)      # Empty array for the IS
iLM = np.zeros(Y_size)      # Empty array for the LM
# IS Parameters
a = 100                     # Autonomous consumption
b = 0.2                     # Marginal propensity to consume
alpha = 5                   # Autonomous imports
beta  = 0.15                # Marginal propensity to import
T = 1                       # Taxes
I = 10                      # Investment intercept (when i = 0)
G = 20                      # Government spending
X = 5                       # Exports (given)
d = 2                       # Investment slope wrt to i
# LM Parameters
c1 = 2500                   # Precautionary money demand
c2 = 0.75                   # Transaction money demand
c3 = 5                      # Speculation money demand
Ms = 23500                  # Nominal money supply
P  = 10                     # Price level

"3|DEFINE AND POPULATE THE IS AND LM SCHEDULES"
def i_IS(a, alpha, b, beta, T, I, G, X, d, Y):
    i_IS = ((a-alpha)-(b-beta)*T + I + G + X - (1-b+beta)*Y)/d
    return i_IS

def i_LM(c1, c2, c3, Ms, P, Y):
    i_LM = (c1 - Ms/P)/c3 + c2/c3*Y
    return i_LM

for j in range(0, Y_size):
    iIS[j] = i_IS(a, alpha, b, beta, T, I, G, X, d, j)
    iLM[j] = i_LM(c1, c2, c3, Ms, P, j)

"4|CALCULATE EQUILIBRUM VALUES"
Y_star1 = ((a-alpha) - (b-beta)*T + I + G + X)/d
Y_star2 = (1/c3) * (c1 - Ms/P)
Y_star3 = (1 - b + beta)/d + (c2/c3)
Y_star  = (Y_star1 - Y_star2)/Y_star3

i_star1 = (1/c3)*(c1 - Ms/P)
i_star2 = (c2/c3)*Y_star
i_star  = i_star1 + i_star2

"5|CALCULATE THE DYNAMICS FOR DISEQUILIBRIUM POINTS"
iterations= 10
def Y_IS(a, alpha, b, beta, T, I, G, X, d, i):
    Y_IS = ((a-alpha)-(b-beta)*T+I+G+X)/(1-b+beta) - d/(1-b+beta)*i
    return Y_IS

" |STARTING POINT A"
YA = 10
iA = 50

A_i_LM = np.zeros(iterations)
A_Y_IS = np.zeros(iterations)

A_Y_IS[0] = YA
A_i_LM[0] = iA

for j in range(1, iterations):
    A_Y_IS[j] = Y_IS(a, alpha, b, beta, T, I, G, X, d, A_i_LM[j-1])
    A_i_LM[j] = i_LM(c1, c2, c3, Ms, P, A_Y_IS[j-1])
    
" |STARTING POINT B"
YB = 80
iB = 55

B_i_LM = np.zeros(iterations)
B_Y_IS = np.zeros(iterations)

B_Y_IS[0] = YB
B_i_LM[0] = iB

for j in range(1, iterations):
    B_Y_IS[j] = Y_IS(a, alpha, b, beta, T, I, G, X, d, B_i_LM[j-1])
    B_i_LM[j] = i_LM(c1, c2, c3, Ms, P, B_Y_IS[j-1])   
    
" |STARTING POINT C"
YC = 70
iC = 20

C_i_LM = np.zeros(iterations)
C_Y_IS = np.zeros(iterations)

C_Y_IS[0] = YC
C_i_LM[0] = iC

for j in range(1, iterations):
    C_Y_IS[j] = Y_IS(a, alpha, b, beta, T, I, G, X, d, C_i_LM[j-1])
    C_i_LM[j] = i_LM(c1, c2, c3, Ms, P, C_Y_IS[j-1])    

" |STARTING POINT D"
YD = 30
iD = 25

D_i_LM = np.zeros(iterations)
D_Y_IS = np.zeros(iterations)

D_Y_IS[0] = YD
D_i_LM[0] = iD

for j in range(1, iterations):
    D_Y_IS[j] = Y_IS(a, alpha, b, beta, T, I, G, X, d, D_i_LM[j-1])
    D_i_LM[j] = i_LM(c1, c2, c3, Ms, P, D_Y_IS[j-1])

"6|PLOT THE IS-LM model"
y_max = np.max(iIS)
v = [0, Y_size, 0, y_max]                       # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="IS-LM MODEL", xlabel=r'Y', ylabel=r'r')
ax.plot(Y, iIS, "k-")
ax.plot(Y, iLM, "k-")
ax.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
plt.plot(Y_star, i_star, "ko")                  # Equilibrium point
plt.plot(YA, iA, "bo")                          # Starting point A
ax.plot(A_Y_IS, A_i_LM, "b--", alpha=0.7)
plt.plot(YB, iB, "ro")                          # Starting point B
ax.plot(B_Y_IS, B_i_LM, "r--", alpha=0.7)
plt.plot(YC, iC, "go")                          # Starting point C
ax.plot(C_Y_IS, C_i_LM, "g--", alpha=0.7)
plt.plot(YD, iD, "co")                          # Starting point C
ax.plot(D_Y_IS, D_i_LM, "c--", alpha=0.7)
plt.axvline(x=Y_star, ls=':', color='k')
plt.axhline(y=i_star, ls=':', color='k')
plt.text(95, 22, "IS")
plt.text(95, 47, "LM")
plt.text(YA  , iA+2, "A", color="b")
plt.text(YB+3, iB  , "B", color="r")
plt.text(YC-3, iC  , "C", color="g")
plt.text(YD  , iD-2, "D", color="c")
plt.axis(v)                                     # Use 'v' as the axes range
plt.show()
