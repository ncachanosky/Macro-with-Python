"|===========================================================================|"
"|===========================================================================|"
"|MACROECONOMICS WITH PYTHON: LABOR MARKET                                   |"
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
size = 50                        # Real wage domain
K = 20                           # Capital stock
A = 20                           # Technology
alpha = 0.6                      # Output elasticity of capital
# Arrays
rW = np.arange(size)             # Real wage
Nd = np.zeros(size)              # Labor demand

"3|LABOR DEMAND FUNCTION"
def N_demand(A, K, rW, alpha):
    Nd = K * ((1-alpha)*A/rW)**(1/alpha)
    return Nd

"4|CALCULATE LABOR DEMAND AND SHOCK EFFECTS"
Nd_K = np.zeros(size)    # Create empty array of capital shock
Nd_A = np.zeros(size)    # Create empty array of productivity shock
Nd_a = np.zeros(size)    # Create empty array of output elasticity of K shock

D_K = 20
D_A = 20
D_a = 0.2

for i in range(1, size):
    Nd[i]   = N_demand(A    , K    , i, alpha)
    Nd_K[i] = N_demand(A    , K+D_K, i, alpha)
    Nd_A[i] = N_demand(A+D_A, K    , i, alpha)
    Nd_a[i] = N_demand(A    , K    , i, alpha + D_a)
    
"5|PLOT LABOR DEMAND AND SHOCK EFFECTS"
xmax_v = np.zeros(4)
xmax_v[0] = np.max(Nd)
xmax_v[1] = np.max(Nd_K)
xmax_v[2] = np.max(Nd_A)
xmax_v[3] = np.max(Nd_a)
xmax = np.max(xmax_v)

v = [0, 30, 0, size]                            # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="LABOR DEMAND", xlabel=r'Nd', ylabel=r'w/P')
ax.grid()
ax.plot(Nd[1:size]  , rW[0:size-1], "k-", label="Labor demand", linewidth=3)
ax.plot(Nd_K[1:size], rW[0:size-1], "b-", label="Capital shock")
ax.plot(Nd_A[1:size], rW[0:size-1], "r-", label="Productivity shock")
ax.plot(Nd_a[1:size], rW[0:size-1], "g-", label="Output elasticity of K shock")
ax.yaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())   # Hide ticks
ax.legend() 
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
T = 25                           # Available hours to work
beta = 0.7                       # Utility elasticity of consumption
I = 50                           # Non-labor income
L = np.arange(T)                 # Array of labor hours from 0 to T
C = np.zeros(T)                  # Empty array of consumption
B = np.zeros(T)                  # Empty array for the budget constraint
rW = 25                          # Real wage

"3|CALCULATE OPTIMAL VALUES AND DEFINE FUNCTIONS"
Ustar = (beta*(I+24*rW))**beta * ((1-beta)*(I+24*rW)/rW)**(1-beta)
Lstar = (1-beta)*((I+24*rW)/rW)
Cstar = beta*(I+24*rW)

def C_indff(U, L, beta):         # Create consumption function
    C_indiff = (U/L**(1-beta))**(1/beta)
    return C_indiff

def Budget(I, rW, L):            # Create budget constraint
    Budget = (I + 24*rW) - rW*L
    return Budget

B[0] = Budget(I, rW, 0)
for t in range(1,T):
    C[t] = C_indff(Ustar, L[t], beta)
    B[t] = Budget(I, rW, L[t])        

"4|PLOT THE INDIFFERENCE CURVE AND THE BUDDGET CONSTRAINT"
y_max = 2*Budget(I, rW, 0)

v = [0, T, 0, y_max]                               # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="INDIFFERENCE CURVE", xlabel="Leisure", ylabel="Real income")
ax.grid()
ax.plot(L[1:T], C[1:T], "g-", label="Indifference curve")
ax.plot(L[0:T], B[0:T], "k-", label="Budget constraint")
plt.axvline(x=T-1  , ymin=0, ymax=I/y_max, color='k') # Add non-labor income
plt.axvline(x=Lstar, ymin=0, ymax = Cstar/y_max, ls=':', color='k') # Lstar
plt.axhline(y=Cstar, xmin=0, xmax = Lstar/T    , ls=':', color='k') # Cstar
plt.plot(Lstar, Cstar, 'bo')                                        # Point
plt.text(0.1      ,  Cstar+5, np.round(Cstar, 1), color="k")
plt.text(Lstar+0.2,  10     , np.round(Lstar, 1), color="k")
ax.legend() 
plt.axis(v)                                         # Use 'v' as the axes range
plt.show()


#%%
"|***************************************************************************|"
"|CELL #3|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library

"2|DEFINE PARAMETERS AND ARRAYS"
size = 50
T = 25                           # Available hours to work
beta = 0.6                       # Utility elasticity of consumption
I = 50                           # Non-labor income
rW   = np.arange(size)           # Vector of real wages
Ns   = np.zeros(size)            # Array of labor hours from 0 to T
Ns_I = np.zeros(size)            # Shock to non-labor income
Ns_b = np.zeros(size)            # Shock to consumption elasticity of utility

"3|LABOR SUPPLY"
def Lsupply(rW, beta, I):
    Lsupply = 24 - (1-beta)*((24*rW + I)/rW)
    return Lsupply

I_shock = 25
b_shock = 0.10
for i in range(1,size):
    Ns[i]   = Lsupply(i, beta, I)
    Ns_I[i] = Lsupply(i, beta, I+I_shock)
    Ns_b[i] = Lsupply(i, beta+b_shock, I)
    
"4|PLOT LABOR SUPPLY"
y_max = np.max(Ns)

v = [0, T, 0, y_max]                               # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="LABOR SUPPLY", xlabel="Work Hs.", ylabel=r'(w/P)')
ax.grid()
ax.plot(Ns[1:T]  , rW[1:T], "k", label="Labor supply", linewidth=3)
ax.plot(Ns_I[1:T], rW[1:T], "b", label="Non-labor income shock")
ax.plot(Ns_b[1:T], rW[1:T], "r", label="Consumption elasticy of utility shock")
ax.yaxis.set_major_locator(plt.NullLocator())      # Hide ticks
ax.xaxis.set_major_locator(plt.NullLocator())      # Hide ticks
ax.legend() 
plt.axis(v)                                        # Use 'v' as the axes range
plt.show()


#%%
"|***************************************************************************|"
"|CELL #4|*******************************************************************|"
"|***************************************************************************|"
"1|IMPORT PACKAGES"
import numpy as np               # Package for scientific computing with Python
import matplotlib.pyplot as plt  # Matplotlib is a 2D plotting library
from scipy.optimize import root  # Package to find the roots of a function

"2|DEFINE PARAMETERS AND ARRAYS"
size = 50
T = 24                           # Available hours to work
# Demand parameters
K = 20                           # Capital stock
A = 20                           # Total factor productivity
alpha = 0.6                      # Output elasticity of capital
Nd   = np.zeros(T)               # Array of labor demand
# Supply parameters
I = 50                           # Non-labor income
beta = 0.6                       # Utility elasticity of consumption
Ns   = np.zeros(size)            # Array of labor supply
# Arrays
rW = np.arange(size)             # Real wage
Nd = np.zeros(size)              # Labor demand
Ns = np.zeros(size)              # Labor supply

"3|OPTIMIZATION PROBLEM: FIND EQUILIBRIUM VALUES"
def Ndemand(A, K, rW, alpha):
    Nd = K * ((1-alpha)*A/rW)**(1/alpha)
    return Nd

def Nsupply(rW, beta, I):
    Lsupply = T - (1-beta)*((24*rW + I)/rW)
    return Lsupply

def Eq_Wage(rW):
    Eq_Wage = Ndemand(A, K, rW, alpha) - Nsupply(rW, beta, I)
    return Eq_Wage

rW_0 = 10
rW_star = root(Eq_Wage, rW_0)
N_star = Nsupply(rW_star.x, beta, I)

"4|PLOT LABOR MARKET EQUILIBRIUM"
for i in range(1, size):
    Nd[i] = Ndemand(A, K, i, alpha)
    Ns[i] = Nsupply(i, beta, I)

y_max = rW_star.x*2
v = [0, T, 0, y_max]                               # Set the axes range
fig, ax = plt.subplots(figsize=(10, 8))
ax.set(title="LABOR SUPPLY", xlabel="Work Hs.", ylabel=r'(w/P)')
ax.plot(Ns[1:T], rW[1:T], "k", label="Labor supply")
ax.plot(Nd[1:T], rW[1:T], "k", label="Labor demand")
plt.plot(N_star, rW_star.x, 'bo') 
plt.axvline(x=N_star   , ymin=0, ymax=rW_star.x/y_max, ls=':', color='k')
plt.axhline(y=rW_star.x, xmin=0, xmax=N_star/T       , ls=':', color='k')
plt.text(5 , 20, "Labor demand")
plt.text(19,  9, "Labor supply")
plt.text(0.2       , rW_star.x+0.5, np.round(rW_star.x, 1))
plt.text(N_star+0.3, 0.3          , np.round(N_star, 1))
plt.axis(v)                                         # Use 'v' as the axes range
plt.show()